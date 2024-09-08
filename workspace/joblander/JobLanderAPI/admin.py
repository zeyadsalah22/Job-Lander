from django.contrib import admin
from .models import Company, Employee, Application, Question

# Register your models here.
admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Application)
admin.site.register(Question)
