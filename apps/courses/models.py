from django.db import models
from apps.subjects.models import Subject

# Create your models here.
class Course(models.Model):
    name=models.CharField(verbose_name="Nombre del curso",max_length=100)
    subjects=models.ManyToManyField(Subject,verbose_name="Asignaturas",related_name="course_subject")
    
    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering=['-id']