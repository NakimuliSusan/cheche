from django.urls import path
from . import views

urlpatterns = [
    path('teachers',views.TeacherAPIView.as_view() ),
    path('teacher-detail/<int:id>', views.TeacherDetailAPIView.as_view()),
    path('teacher/<int:id>', views.GenericAPIView.as_view()),
    path('teacher', views.GenericAPIView.as_view()),
    
]