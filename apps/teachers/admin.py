from django.contrib import admin
from .models import Teacher, TeacherSubject
# Register your models here.

class TeacherAdmin(admin.ModelAdmin):
    fields=(('first_name','last_name','identification','gender'),'address')
    list_display=('id','nombre_completo','user')
    list_display_links=('id','nombre_completo',)
    #list_filter=('courses','subjects',)
    #filter_horizontal=('subjects','courses',)
    
    def nombre_completo(self,obj):
        return "{0} {1}".format(obj.first_name,obj.last_name)
    
    nombre_completo.eempty_value_display = 'Desconocido'

admin.site.register(Teacher, TeacherAdmin)
admin.site.register(TeacherSubject)
