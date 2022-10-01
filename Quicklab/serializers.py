from rest_framework import serializers
from . import models

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields=['first_name','last_name','username','password', 'email','level']