from django.contrib import admin
from .models import Faculty_db,Student_db,Finance_db

# Register your models here.

admin.site.register(Faculty_db)
admin.site.register(Student_db)
admin.site.register(Finance_db)