from rest_framework import serializers
from . import models

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields=['first_name','last_name','username','password', 'email']
        
        
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ( 'first_name', 'last_name', 'username','email','password')
        extra_kwargs = {'password': {'write_only': True}}
        

class LoginSerializer(serializers.Serializer):
    # username = serializers.CharField()
    # password = serializers.CharField()

    class Meta:
        model = models.Teacher
        fields = ('username', 'password')
    def create(self, validated_data):
        teacher = models.Teacher.objects.create_user(validated_data['username'], validated_data['password'])
        return teacher



