from rest_framework import serializers
from django.contrib.auth.models import User

from . import models

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields=['first_name','last_name','username','password', 'email']
        
        
class TeacherRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = ( 'first_name', 'last_name', 'username','password','email')
        extra_kwargs = {'password': {'write_only': True}}
        
def create(self, validated_data):
        user = models.Teacher.objects.create(validated_data['username'], validated_data['password'],)
        return user



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields=['first_name', 'last_name','username', 'password','level','no_of_practicals']


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ( 'first_name', 'last_name', 'username','password','level')
        extra_kwargs = {'password': {'write_only': True}}
def create(self, validated_data):
        user = models.Student.objects.create(validated_data['username'], validated_data['password'],)
        return user
