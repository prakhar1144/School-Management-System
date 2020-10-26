from django.views.generic import TemplateView, ListView, DetailView
from .models import Faculty_db,Student_db,Staff_db 
from django.shortcuts import render
from datetime import date

# Create your views here.
class Home(TemplateView):
	template_name = 'main/home.html'

class Faculty(ListView):
	model = Faculty_db
	template_name = 'main/faculty.html'

class Faculty_detail(DetailView):
	model = Faculty_db
	context_object_name = 'faculty_name'
	template_name = 'main/details.html'

class Student(ListView):
	queryset = Student_db.options
	context_object_name = 'classes'
	template_name = 'main/student.html'

def Class_detail(request, i):
	cdetail = list(Student_db.objects.filter(Class=i))
	return render(request, 'main/student_details.html',{'cdetail':cdetail})

class Finance(ListView):
	queryset = Student_db.options
	context_object_name = 'classes'
	template_name = 'main/finance.html'

def Student_finance(request, i):
	# Due_Student = []
	cdetail = list(Student_db.objects.filter(Class=i))
	# for j  in cdetail:
	# 	due = (j.Fee.Paid_Till.year - j.Fee.Joined.year)*12 + (j.Fee.Paid_Till.month - j.Fee.Joined.month)
	# 	if due > 0:
	# 		Due_Student.append(j) 

	return render(request, 'main/student_finance.html',{'cdetail':cdetail,'Standard':i})

def Due_detail(request, i):
	Due_Student = []
	cdetail = list(Student_db.objects.filter(Class=i))
	for j  in cdetail:
		due = (date.today().year -j.Fee.Paid_Till.year)*12 + (date.today().month - j.Fee.Paid_Till.month)
		if due > 0:
			Due_Student.append(j) 
	
	return render(request, 'main/student_due.html',{'Due_Student':Due_Student})

class Staff(ListView):
	model = Staff_db
	template_name = 'main/staff.html'

class Staff_detail(DetailView):
	model = Staff_db
	context_object_name = 'staff_name'
	template_name = 'main/staff_detail.html'

class Faculty_finance(ListView):
	model = Faculty_db
	context_object_name = 'faculty_name'
	template_name = 'main/faculty_finance.html'

class Staff_finance(ListView):
	model = Staff_db
	context_object_name = 'staff_name'
	template_name = 'main/staff_finance.html'

class SearchResultStudentView(ListView):
	model = Student_db
	template_name = 'main/search_result.html'
	context_object_name = 'Student_list'

	def get_queryset(self):
		query = self.request.GET.get('q')
		Student_list = Student_db.objects.filter(Name__icontains = query)
		return Student_list

class SearchResultFacultyView(ListView):
	model = Faculty_db
	template_name = 'main/search_result.html'
	context_object_name = 'Faculty_list'

	def get_queryset(self):
		query = self.request.GET.get('q')
		Faculty_list = Faculty_db.objects.filter(Name__icontains = query)
		return Faculty_list

class SearchResultStaffView(ListView):
	model = Staff_db
	template_name = 'main/search_result.html'
	context_object_name = 'Staff_list'

	def get_queryset(self):
		query = self.request.GET.get('q')
		Staff_list = Staff_db.objects.filter(Name__icontains = query)
		return Staff_list