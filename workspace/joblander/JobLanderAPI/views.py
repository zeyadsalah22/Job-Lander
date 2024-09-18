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
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = ['name']
    search_fields = ['name', 'job_title', 'company__name', 'contacted']
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        return Employee.objects.filter(user=self.request.user)
    
class SingleEmployeeView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Employee.objects.filter(id=self.kwargs['pk'], user=self.request.user)
    

class ApplicationsView(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = ['submission_date']
    search_fields = ['job_title', 'company__name', 'status']
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        return Application.objects.filter(user=self.request.user)
    
class SingleApplicationView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationDetailsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Application.objects.filter(id=self.kwargs['pk'], user=self.request.user)
    
class QuestionsView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = ['application__submission_date']
    search_fields = ['question', 'application__job_title', 'application__company__name']
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        return Question.objects.filter(user=self.request.user)
    
class SingleQuestionView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Question.objects.filter(id=self.kwargs['pk'], user=self.request.user)