from django.views.generic import TemplateView, ListView, DetailView
from .models import Faculty_db 

# Create your views here.
class Home(TemplateView):
	template_name = 'main/home.html'

class Faculty(ListView):
	model = Faculty_db
	template_name = 'main/faculty.html'

class Faculty_detail(DetailView):
	queryset = Faculty_db.objects.all()
	context_object_name = 'faculty_name'
	template_name = 'main/details.html'