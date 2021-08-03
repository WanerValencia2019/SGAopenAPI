from django.db import models
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.courses.models import Course


from apps.users.models import PropertyUser

User = get_user_model()

# Create your models here.
class Student(PropertyUser):
    course=models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name="Curso",related_name="student_course", null=True, blank=True)

    def __str__(self):
        return "{}-{}".format(self.id,self.get_fullName())
    
    def get_fullName(self):
        return "{} {}".format(self.first_name,self.last_name)
    
    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"

@receiver(post_save, sender=Student)
def create_profile_student(sender,instance,**kwargs):    
    if instance.user is None:
        first_name,last_name=instance.first_name,instance.last_name
        email=first_name.split(" ")[0][:3].lower()+last_name.split(" ")[0].lower()+"@sgaone.edu.co"
        username=first_name[:3].lower()+last_name.split(" ")[0].lower()
        password="SGAOPEN2021"
        
        createGroup,group=Group.objects.get_or_create(name="ESTUDIANTES")
        create_user=User()        
        create_user.username=username
        create_user.first_name=first_name
        create_user.last_name=last_name
        create_user.email=email
        create_user.set_password(password)
        create_user.save()
        if group is None:
            create_user.groups.set([createGroup])  
        else:
            create_user.groups.set([group])  
        instance.user=create_user
        instance.save()    