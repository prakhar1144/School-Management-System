from django.urls import path
from .views import Home,Faculty,Faculty_detail,Student, Class_detail,Finance,Student_finance,Due_detail,Staff,Staff_detail,Faculty_finance,Staff_finance,SearchResultStudentView,SearchResultFacultyView,SearchResultStaffView

urlpatterns = [

path('', Home.as_view() , name= 'home'),
path('faculty/', Faculty.as_view(), name= 'faculty'),
path('faculty/<int:pk>/', Faculty_detail.as_view(), name='faculty_detail'),
path('student/', Student.as_view(), name = 'student'),
path('class_detail/<i>/', Class_detail, name = 'class_detail'),
path('finance/', Finance.as_view(), name = 'finance'),
path('finance/<i>', Student_finance, name = 'finance_detail'),
path('due_detail/<i>', Due_detail, name = 'Due_detail'),
path('staff/', Staff.as_view(), name= 'staff'),
path('staff/<int:pk>/', Staff_detail.as_view(), name='staff_detail'),
path('finance/faculty/', Faculty_finance.as_view() , name='teacher_finance'),
path('finance/staff/', Staff_finance.as_view() , name='staff_finance'),
path('search/student/', SearchResultStudentView.as_view(), name='search_result_student'),
path('search/faculty/', SearchResultFacultyView.as_view(), name='search_result_faculty'),
path('search/staff/', SearchResultStaffView.as_view(), name='search_result_staff'),
# path('search/class/', SearchResultFacultyView.as_view(), name='search_result_faculty'),
]