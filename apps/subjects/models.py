from django.db import models

# Create your models here.

class Subject(models.Model):
    subject=models.CharField(verbose_name="Asignatura",max_length=100,blank=False)
    
    def __str__(self):
        return self.subject 
    
    class Meta:
        verbose_name = 'Asignatura'
        verbose_name_plural = 'Asignaturas'
        ordering=['-id']