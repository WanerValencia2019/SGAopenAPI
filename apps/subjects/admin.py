from django.contrib import admin
from .models import Subject
# Register your models here.

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject',)


admin.site.register(Subject, SubjectAdmin)
