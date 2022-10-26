from django.urls import path
from . import views


urlpatterns = [
    path('teachers/',views.TeacherRegisterViewSet.as_view(), name='teachers' ),
    path('login/', views.LoginAPI.as_view(), name='login'),
    path('students',views.StudentRegisterViewset.as_view(),name='students'),
    path('practicals/',views.PracticalViewset.as_view(), name='practicals' ),
    path('instructions/',views.InstructionViewset.as_view(), name='instructions' ),
    
]