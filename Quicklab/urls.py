from django.urls import path
from . import views
from knox import views as knox_views


urlpatterns = [
    # path('article', article_list),
    # path('article/<int:pk>', article_detail),
    path('students',views.studentApi,name='students'),
    # path('students-detail/<int:id>', views.StudentDetailAPIView.as_view()),
    # path('student/<int:id>', views.GenericAPIView.as_view()),
    # path('student', views.GenericAPIView.as_view()),
    path('register/',views.RegisterAPI.as_view(), name='register'),
    path('login/', views.LoginAPI.as_view(), name='login'),
    path('Quicklab/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('Quicklab/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]