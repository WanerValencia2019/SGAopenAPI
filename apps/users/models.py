from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from apps.courses.models import Course
from django.dispatch import receiver

User = get_user_model()

# Create your models here.
class PropertyUser(models.Model):    
    FEMALE='FM'
    MALE='MA'
    GENDER = [
        (FEMALE, 'Femenino'),
        (MALE, 'Masculino'),
    ]
    identification=models.CharField(verbose_name="Identificación",max_length=11, blank=False,db_index=True,)
    first_name=models.CharField(verbose_name="Nombre",max_length=100)
    last_name=models.CharField(verbose_name="Apellidos",max_length=100)
    personal_email = models.EmailField(verbose_name="Correo personal")
    gender = models.CharField(
        max_length=2,
        choices=GENDER,
        default="MA",
        null=False,
        blank=False,
        verbose_name="Género"
    )
    created_at=models.DateTimeField(auto_now_add=True,verbose_name="Creado")
    update_at=models.DateField(auto_now=True,verbose_name="Actualizado")
    user=models.OneToOneField(User,on_delete=models.CASCADE,verbose_name="Perfil",null=True)

    class Meta:
       abstract = True


class Student(PropertyUser):
    course=models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name="Curso",related_name="student_course", null=True, blank=True)

    def __str__(self):
        return "{}-{}".format(self.id,self.get_fullName())
    
    def get_fullName(self):
        return "{} {}".format(self.first_name,self.last_name)

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
    


