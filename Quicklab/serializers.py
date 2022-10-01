from rest_framework import serializers
from . import models

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields=['first_name', 'last_name', 'email', 'password','level','no_of_practicals']