from django.views.generic import TemplateView, ListView, DetailView
from .models import Faculty_db,Student_db 
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

def Finance_detail(request, i):
	# Due_Student = []
	cdetail = list(Student_db.objects.filter(Class=i))
	# for j  in cdetail:
	# 	due = (j.Fee.Paid_Till.year - j.Fee.Joined.year)*12 + (j.Fee.Paid_Till.month - j.Fee.Joined.month)
	# 	if due > 0:
	# 		Due_Student.append(j) 

	return render(request, 'main/finance_detail.html',{'cdetail':cdetail,'Standard':i})

def Due_detail(request, i):
	Due_Student = []
	cdetail = list(Student_db.objects.filter(Class=i))
	for j  in cdetail:
		due = (date.today().year -j.Fee.Paid_Till.year)*12 + (date.today().month - j.Fee.Paid_Till.month)
		if due > 0:
			Due_Student.append(j) 
	
	return render(request, 'main/temporary.html',{'Due_Student':Due_Student})