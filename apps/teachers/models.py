from django.db import models
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.subjects.models import Subject
from apps.courses.models import Course
from apps.users.models import PropertyUser


User = get_user_model()
# Create your models here.

class Teacher(PropertyUser):
    address = models.CharField(max_length=150, verbose_name="Dirección")

    def __str__(self):
        return "{} {}".format(self.first_name,self.last_name)
    
    class Meta:
        verbose_name = 'Docente'
        verbose_name_plural = 'Docentes'
        ordering=['-id']

@receiver(post_save, sender=Teacher)
def create_profile_teacher(sender,instance,**kwargs):
    first_name,last_name=instance.first_name,instance.last_name
    if instance.user is None:
        email=first_name.split(" ")[0].lower()+"."+last_name.split(" ")[0].lower()+"@sgateacher.edu.co"
        username=first_name.split(" ")[0].lower()+last_name.split(" ")[0].lower()
        password="SGAOPEN2021"        
        create_user=User.objects.create_user(username, email, password)
        create_user.first_name=first_name
        create_user.last_name=last_name
        create_user.save() 
        instance.user=create_user
        instance.save()



class TeacherSubject(models.Model):
    teacher = models.ForeignKey("Teacher", on_delete=models.CASCADE, related_name="_teacher_subject", null=True, blank=True)    
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="_subject")


    def __str__(self):
        return f"{self.teacher.user.username} - {self.course.name} - {self.subject}"
    
    class Meta:
        verbose_name = "Teacher Subject"
        verbose_name_plural = "Teacher Subjects"