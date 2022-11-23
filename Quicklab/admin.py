from django.contrib import admin
from . import models

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username', 'level','no_of_practicals') 
    search_fields = ('first_name', 'last_name')
admin.site.register(models.Student, StudentAdmin)

class TeacherAdmin(admin.ModelAdmin):
     list_display = ('first_name', 'last_name', 'username', 'email') 
     search_fields = ('first_name', 'last_name')
admin.site.register(models.Teacher, TeacherAdmin)

class PracticalAdmin(admin.ModelAdmin):
     list_display = ('description', 'title', 'tools', 'status','comments') 
     search_fields = ('description', 'status', 'comments')
admin.site.register(models.Practical, PracticalAdmin)

class ToolsAdmin(admin.ModelAdmin):
     list_display = ('label', 'subject', 'image') 
     search_fields = ('label', 'subject', 'image')
admin.site.register(models.Tool, ToolsAdmin)

class InstructionsAdmin(admin.ModelAdmin):
     list_display = (  'instruction_title', 'image') 
     search_fields = ( 'instruction_title', 'image')
admin.site.register(models.Instruction, InstructionsAdmin)


