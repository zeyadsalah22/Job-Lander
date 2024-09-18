from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from .pagination import CustomPageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.db.models import Count, Q
from rest_framework.views import APIView
from rest_framework.response import Response

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
    
class StatisticsView(APIView):
    def get(self, request, *args, **kwargs):
        user = request.user
        
        # Aggregate in a single query
        stats = Application.objects.filter(user=user).aggregate(
            total_applications=Count('id'),
            pending_applications=Count('id', filter=~Q(status=ApplicationStatus.REJECTED.name) & ~Q(status=ApplicationStatus.ACCEPTED.name)),
            rejected_applications=Count('id', filter=Q(status=ApplicationStatus.REJECTED.name)),
            accepted_offers=Count('id', filter=Q(status=ApplicationStatus.ACCEPTED.name)),
        )

        return Response(stats)
    
class PercentsView(APIView):
    def get(self, request, *args, **kwargs):
        user = request.user
        
        # Aggregate in a single query
        stats = Application.objects.filter(user=user, status__in=[ApplicationStatus.ACCEPTED.name, ApplicationStatus.REJECTED.name]).aggregate(
            total_applications=Count('id'),
            applied_stage=Count('id', filter=Q(stage=Stage.APPLIED.name)),
            phonescreen_stage=Count('id', filter=Q(stage=Stage.PHONE_SCREEN.name)),
            assessment_stage=Count('id', filter=Q(stage=Stage.ASSESSMENT.name)),
            interview_stage=Count('id', filter=Q(stage=Stage.INTERVIEW.name)),
            offer_stage=Count('id', filter=Q(stage=Stage.OFFER.name)),
        )

        total = stats['total_applications']
        for key in stats:
            stats[key] = round((stats[key]/total)*100, 2)

        return Response(stats)