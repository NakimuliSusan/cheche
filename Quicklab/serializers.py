from rest_framework import serializers
from . import models

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
        student = models.Student.objects.create_Student(validated_data['username'], validated_data['password'],)

        return student