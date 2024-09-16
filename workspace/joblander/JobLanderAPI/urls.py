from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('companies', views.CompaniesView.as_view(), name='companies'),
    path('companies/<int:pk>', views.SingleCompanyView.as_view(), name='single_company'),
    path('employees', views.EmployeesView.as_view(), name='employees'),
    path('employees/<int:pk>', views.SingleEmployeeView.as_view(), name='single_employee'),
]