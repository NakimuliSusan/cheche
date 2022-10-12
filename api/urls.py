from django.urls import path
from . import views


urlpatterns = [
    path('teachers/',views.TeacherRegisterViewSet.as_view(), name='teachers' ),
    path('login/', views.LoginAPI.as_view(), name='login'),
    # path('registerteacher/', views.TeacherRegisterViewSet.as_view(), name='registerTeacher'),
    path('students',views.StudentRegisterViewset.as_view(),name='students'),
    # path('register/',views.RegisterAPI.as_view(), name='register'),
    path('practicals/',views.PracticalViewset.as_view(), name='practicals' ),
    # path('Quicklab/logout/', knox_views.LogoutView.as_view(), name='logout'),
    # path('Quicklab/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    
]