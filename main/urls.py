from django.urls import path
from .views import Home,Faculty,Faculty_detail,Student, Class_detail,Finance

urlpatterns = [

path('', Home.as_view() , name= 'home'),
path('faculty/', Faculty.as_view(), name= 'faculty'),
path('faculty/<int:pk>/', Faculty_detail.as_view(), name='faculty_detail'),
path('student/', Student.as_view(), name = 'student'),
path('class_detail/<i>/', Class_detail, name = 'class_detail'),
path('finance/', Finance.as_view(), name = 'finance')
]