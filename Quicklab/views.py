from rest_framework.authtoken.models import Token
from django.shortcuts import render
from requests import request
from . import models
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from . import serializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.response import Response
from knox.models import AuthToken
from rest_framework import generics, permissions
from django.contrib.auth import login,authenticate
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken




<<<<<<< HEAD
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



class RegisterAPI(generics.GenericAPIView):
    serializer_class = serializers.RegisterSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        teacher = serializer.save()
        User.objects.create_user(username=teacher.username , password=teacher.password)
        return Response({
        "teacher": serializers.TeacherSerializer(teacher, context=self.get_serializer_context()).data,
        # "token": AuthToken.objects.create(student)[1]
        })

    
    
class LoginAPI(KnoxLoginView):
    serializer_class = serializers.LoginSerializer
    # permission_classes = (permissions.AllowAny,)



    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        teacher = serializer.validated_data
        token=AuthToken.objects.create(teacher)[1]
        
        return Response({
            'teacher':serializers.TeacherSerializer(teacher, context=self.get_serializer_context()).data,
            'token':token
        })


# class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,  mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
#     serializer_class = serializers.TeacherSerializer
#     queryset = models.Teacher.objects.all()
=======
# class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,  mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
#     serializer_class = serializers.StudentSerializer
#     queryset = models.Student.objects.all()
>>>>>>> dedd2ab8953559fe6520e22b91c4a9a29c09e77f
#     lookup_field = "id"

#     #authentication_classes = [SessionAuthentication, BasicAuthentication]
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request, id=None):
#         if id:
#             return self.retrieve(request)
#         else:
#             return self.list(request)

#     def post(self,request):
#         return self.create(request)

#     def put(self, request, id=None):
#         return self.update(request, id)

#     def delete(self, request, id):
#         return self.destroy(request, id)


<<<<<<< HEAD
# class TeacherAPIView(APIView):
#     def get(self, request):
#         teachers = models.Teacher.objects.all()
#         serializer = serializers.TeacherSerializer(teachers, many=True)
=======
# class StudentAPIView(APIView):
#     def get(self, request):
#         students = models.Student.objects.all()
#         serializer = serializers.StudentSerializer(students, many=True)
>>>>>>> dedd2ab8953559fe6520e22b91c4a9a29c09e77f
#         return Response(serializer.data)

#     def post(self, request):
#         data = JSONParser().parse(request)
<<<<<<< HEAD
#         serializer = serializers.TeacherSerializer(data=data)
=======
#         serializer = serializers.StudentSerializer(data=data)
>>>>>>> dedd2ab8953559fe6520e22b91c4a9a29c09e77f

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

<<<<<<< HEAD
# class TeacherDetailAPIView(APIView):
#     def get_object(self, id):
#         try:
#             return models.Teacher.objects.get(id=id)

#         except models.Teacher.DoesNotExist:
#             return HttpResponse(status=status.HTTP_404_NOT_FOUND)

#     def get(self, request, id):
#         teacher = self.get_object(id)
#         serializer = serializers.TeacherSerializer(teacher)
#         return Response(serializer.data)
    
#     def put(self, request, id):
#         teacher = self.get_object(id)
#         serializer = serializers.TeacherSerializer(teacher, data=request.data)
=======
# class StudentDetailAPIView(APIView):
#     def get_object(self, id):
#         try:
#             return models.Student.objects.get(id=id)

#         except models.Student.DoesNotExist:
#             return HttpResponse(status=status.HTTP_404_NOT_FOUND)

#     def get(self, request, id):
#         students = self.get_object(id)
#         serializer = serializers.StudentSerializer(students)
#         return Response(serializer.data)
    
#     def put(self, request, id):
#         students = self.get_object(id)
#         serializer = serializers.StudentSerializer(students, data=request.data)
>>>>>>> dedd2ab8953559fe6520e22b91c4a9a29c09e77f
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, id):
<<<<<<< HEAD
#         teacher = self.get_object(id)
#         teacher.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
=======
#         students = self.get_object(id)
#         students.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

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

        # serializer = AuthTokenSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # student = serializer.validated_data['student']
        # login(request, student)
        # return super(LoginAPI, self).post(request, format=None)
>>>>>>> dedd2ab8953559fe6520e22b91c4a9a29c09e77f
