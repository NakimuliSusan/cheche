from pydoc import visiblename
from rest_framework.authtoken.models import Token
from django.shortcuts import render
from Quicklab import models
from .serializers import *
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from . import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.response import Response
# from knox.models import AuthToken
from rest_framework import generics, permissions, viewsets
from django.contrib.auth import login,authenticate
from rest_framework.authtoken.serializers import AuthTokenSerializer
# from knox.views import LoginView as KnoxLoginView
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken




class TeacherRegisterViewSet(generics.GenericAPIView):
    serializer_class = serializers.TeacherRegisterModelSerializer
    queryset =  models.Teacher.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        teacher = serializer.save()
        User.objects.create_user(username=teacher.username , password=teacher.password)
        return Response({
        "teacher": serializers.TeacherSerializer(teacher, context=self.get_serializer_context()).data,
        # "token": AuthToken.objects.create(student)[1]
        })
    def get(self, request, *args, **kwargs):
        teachers = models.Teacher.objects.all()
        teacher_serializer=serializers.TeacherSerializer(teachers,many=True)
        return JsonResponse(teacher_serializer.data,safe=False)



class StudentRegisterViewset(generics.GenericAPIView):
    serializer_class = serializers.StudentRegisterModelSerializer
    queryset =  models.Student.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        student = serializer.save()
        User.objects.create_user(username=student.username , password=student.password)
        return Response({
        "student": serializers.StudentSerializer(student, context=self.get_serializer_context()).data,
        # "token": AuthToken.objects.create(student)[1]
        })
    def get(self, request, *args, **kwargs):
        students = models.Student.objects.all()
        student_serializer=serializers.StudentSerializer(students,many=True)
        return JsonResponse(student_serializer.data,safe=False)


class PracticalViewset(generics.GenericAPIView): 
    def get(self, request, *args, **kwargs):
        practicals = models.Practical.objects.all()
        practical_serializer=serializers.PracticalSerializer(practicals,many=True)
        return JsonResponse(practical_serializer.data,safe=False)



# Register API
class LoginAPI(ObtainAuthToken):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, ):
        username=request.data['username']
        password=request.data['password']
        user=authenticate(request,username=username, password=password)
        print(user)
        token=Token.objects.create(user=user)
        return Response({
            'body': 'login successful',
            "token": token.key
        })

# class PracticalAPI(generics.GenericAPIView):
#     serializer_class = serializers.PracticalSerializer
#     queryset = models.Practical.objects.all()

