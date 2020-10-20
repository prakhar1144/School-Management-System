from django.views.generic import TemplateView, ListView, DetailView
from .models import Faculty_db,Student_db 
from django.shortcuts import render

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