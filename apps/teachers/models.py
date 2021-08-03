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
    subjects=models.ManyToManyField(Subject,verbose_name="Asignaturas",related_name="teacher_subjects", blank=True)
    courses=models.ManyToManyField(Course,verbose_name="Cursos",related_name="teacher_courses", blank=True)
    def __str__(self):
        return "{} {}".format(self.first_name,self.last_name)
    
    class Meta:
        verbose_name = 'Docente'
        verbose_name_plural = 'Docentes'
        ordering=['-id']

def create_profile_teacher(sender,instance,**kwargs):
    first_name,last_name=instance.first_name,instance.last_name
    if instance.user.id is None:
        email=first_name.split(" ")[0].lower()+"."+last_name.split(" ")[0].lower()+"@sgateacher.edu.co"
        username=first_name.split(" ")[0].lower()+last_name.split(" ")[0].lower()
        password="SGAOPEN2021"

        createGroup,group=Group.objects.get_or_create(name="DOCENTES")
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
