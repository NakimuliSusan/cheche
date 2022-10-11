from django.urls import path
from . import views


urlpatterns = [
    path('teachers/',views.teacherApi, name='teachers' ),
    path('login/', views.LoginAPI.as_view(), name='login'),
    path('registerteacher/', views.TeacherRegisterAPI.as_view(), name='registerTeacher'),
    path('students',views.studentApi,name='students'),
    path('register/',views.RegisterAPI.as_view(), name='register'),
    path('practicals/',views.practicalApi, name='practicals' ),
    # path('Quicklab/logout/', knox_views.LogoutView.as_view(), name='logout'),
    # path('Quicklab/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]