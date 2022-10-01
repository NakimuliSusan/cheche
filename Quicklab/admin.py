from django.contrib import admin
from . import models
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username', 'level','no_of_practicals') 
    search_fields = ('first_name', 'last_name')
admin.site.register(models.Student, StudentAdmin)

class TeacherAdmin(admin.ModelAdmin):
     list_display = ('first_name', 'last_name', 'username', 'email','student') 
     search_fields = ('first_name', 'last_name')
admin.site.register(models.Teacher, TeacherAdmin)

class PracticalsAdmin(admin.ModelAdmin):
     list_display = ('description', 'title', 'tools', 'status','comments') 
     search_fields = ('description', 'status', 'comments')
admin.site.register(models.Practical, PracticalsAdmin)


class ToolsAdmin(admin.ModelAdmin):
     list_display = ('label', 'subject', 'image') 
     search_fields = ('label', 'subject', 'image')
admin.site.register(models.Tool, ToolsAdmin)


