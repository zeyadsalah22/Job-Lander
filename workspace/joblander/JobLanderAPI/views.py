from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from .pagination import CustomPageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Create your views here.
def index(request):
    return render(request, 'index.html')

class CompaniesView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = ['name']
    search_fields = ['name','location']
    pagination_class = CustomPageNumberPagination

class SingleCompanyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Company.objects.filter(id=self.kwargs['pk'])

class EmployeesView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeesSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = ['name']
    search_fields = ['name', 'job_title']
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        return Employee.objects.filter(user=self.request.user)