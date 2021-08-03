from django.contrib import admin

# Register your models here.
from .models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    date_hierarchy="created_at"
    #fields = ['']    
    list_display=['id','first_name','last_name','user']
    list_filter=('course',)
    list_display_links = ('id',)
    list_select_related=('course',)    
    ordering=("first_name","id","created_at",)
    search_fields=("id","first_name","last_name")
    list_per_page=15
    fields=(('first_name','last_name','personal_email','gender'),'course')
    readonly_fields = ('user',)


admin.site.register(Student, StudentAdmin)