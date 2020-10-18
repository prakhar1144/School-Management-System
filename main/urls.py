from django.urls import path
from .views import Home,Faculty,Faculty_detail

urlpatterns = [

path('', Home.as_view() , name= 'home'),
path('faculty/', Faculty.as_view(), name= 'faculty'),
path('faculty/<int:pk>/', Faculty_detail.as_view(), name='faculty_detail'),
]