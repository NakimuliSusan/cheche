from rest_framework.authtoken.models import Token
from django.shortcuts import render
from . import models
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from . import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.response import Response
from knox.models import AuthToken
from rest_framework import generics, permissions
from django.contrib.auth import login,authenticate
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken




@csrf_exempt
def teacherApi(request,id=0):
    if request.method=='GET':
        teachers = models.Teacher.objects.all()
        teacher_serializer = serializers.TeacherSerializer(teachers,many=True)
        return JsonResponse(teacher_serializer.data,safe=False)

    elif request.method=='POST':
        teacher_data = JSONParser().parse(request)
        teacher_serializer = serializers.TeacherSerializer(data=teacher_data)
        if teacher_serializer.is_valid():
            teacher_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to add",safe=False)
    elif request.method=='PUT':
        teacher_data=JSONParser().parse(request)
        teacher = models.Teacher.objects.get(middle_name = teacher_data['middle_name'])
        teacher_serializer=serializers.TeacherSerializer(teacher,data=teacher_data)
        if teacher_serializer.is_valid():
            teacher_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to update",safe=False)
    
    elif request.method=='DELETE':
        teacher=models.Teacher.objects.get(middle_name='middle_name')
        teacher.delete()
        return JsonResponse("Deleted successfully",safe=False)


class TeacherRegisterAPI(generics.GenericAPIView):
    serializer_class = serializers.TeacherRegisterSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        teacher = serializer.save()
        User.objects.create_user(username=teacher.username , password=teacher.password)
        return Response({
        "teacher": serializers.TeacherSerializer(teacher, context=self.get_serializer_context()).data,
        # "token": AuthToken.objects.create(student)[1]
        })

@csrf_exempt
def studentApi(request,id=0):
    if request.method=='GET':
        students = models.Student.objects.all()
        student_serializer = serializers.StudentSerializer(students,many=True)
        return JsonResponse(student_serializer.data,safe=False)
    elif request.method=='POST':
        student_data = JSONParser().parse(request)
        student_serializer = serializers.StudentSerializer(data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to add",safe=False)
    elif request.method=='PUT':
        student_data=JSONParser().parse(request)
        student = models.Student.objects.get(middle_name = student_data['middle_name'])
        student_serializer=serializers.StudentSerializer(student,data=student_data,many=True)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to update",safe=False)
    elif request.method=='DELETE':
        student=models.Student.objects.get(middle_name='middle_name')
        student.delete()
        return JsonResponse("Deleted successfully",safe=False)

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = serializers.RegisterSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        student = serializer.save()
        User.objects.create_user(username=student.username , password=student.password)
        return Response({
        "student": serializers.StudentSerializer(student, context=self.get_serializer_context()).data,
        # "token": AuthToken.objects.create(student)[1]
        })
class LoginAPI(ObtainAuthToken):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        username=request.data['username']
        password=request.data['password']
        user=authenticate(request,username=username, password=password)
        print(user)
        token=Token.objects.create(user=user)
        return Response({
            "token": token.key
        })
