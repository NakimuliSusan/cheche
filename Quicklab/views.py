from django.shortcuts import render
from . import models
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from . import serializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,  mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = serializers.TeacherSerializer
    queryset = models.Teacher.objects.all()
    lookup_field = "id"

    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self,request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)


class TeacherAPIView(APIView):
    def get(self, request):
        teachers = models.Teacher.objects.all()
        serializer = serializers.TeacherSerializer(teachers, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = serializers.TeacherSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeacherDetailAPIView(APIView):
    def get_object(self, id):
        try:
            return models.Teacher.objects.get(id=id)

        except models.Teacher.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        teacher = self.get_object(id)
        serializer = serializers.TeacherSerializer(teacher)
        return Response(serializer.data)
    
    def put(self, request, id):
        teacher = self.get_object(id)
        serializer = serializers.TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        teacher = self.get_object(id)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
