from rest_framework import serializers
from . import models

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields=['first_name','last_name','username','password', 'email']
        

class LoginSerializer(serializers.Serializer):
    # username = serializers.CharField()
    # password = serializers.CharField()

    class Meta:
        model = models.Teacher
        fields = ('username', 'password')
    def create(self, validated_data):
        teacher = models.Teacher.objects.create_user(validated_data['username'], validated_data['password'])
        return teacher



