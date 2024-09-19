from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('companies', views.CompaniesView.as_view(), name='companies'),
    path('companies/<int:pk>', views.SingleCompanyView.as_view(), name='single_company'),
    path('employees', views.EmployeesView.as_view(), name='employees'),
    path('employees/<int:pk>', views.SingleEmployeeView.as_view(), name='single_employee'),
    path('applications', views.ApplicationsView.as_view(), name='applications'),
    path('applications/<int:pk>', views.SingleApplicationView.as_view(), name='single_application'),
    path('questions', views.QuestionsView.as_view(), name='questions'),
    path('questions/<int:pk>', views.SingleQuestionView.as_view(), name='single_question'),
    path('statistics', views.StatisticsView.as_view(), name='statistics'),
    path('percents', views.PercentsView.as_view(), name='percents'),
    path('timeseries', views.TimeSeriesView.as_view(), name='timeseries'),
]