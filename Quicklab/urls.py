from django.urls import path
from . import views


urlpatterns = [
    # path('article', article_list),
    # path('article/<int:pk>', article_detail),
    path('students',views.StudentAPIView.as_view() ),
    path('students-detail/<int:id>', views.StudentDetailAPIView.as_view()),
    path('student/<int:id>', views.GenericAPIView.as_view()),
    path('student', views.GenericAPIView.as_view()),
    
]