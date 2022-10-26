from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from django.contrib.auth.models import User

from Quicklab import models

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields=['first_name','last_name','username','password', 'email']
        
        
class TeacherRegisterModelSerializer(serializers.ModelSerializer):
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
class StudentRegisterModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ( 'first_name', 'last_name', 'username','password','level')
        extra_kwargs = {'password': {'write_only': True}}
def create(self, validated_data):
        user = models.Student.objects.create(validated_data['username'], validated_data['password'],)
        return user

#Practical Serializer
class PracticalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Practical
        fields=['title','description','image','instructions', 'subject']



class InstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Instruction
        fields = ['title','image','practical']


    







