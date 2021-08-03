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



    


