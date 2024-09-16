from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User, Group
from rest_framework.validators import UniqueTogetherValidator, UniqueValidator


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class CompanySerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        validators=[UniqueValidator(queryset=Company.objects.all(), message="Company Already Exists")]
    )
    class Meta:
        model = Company
        fields = '__all__'

class EmployeesSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    company = CompanySerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    company_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Employee
        fields = ['id', 'user', 'name', 'linkedin_link', 'email', 'job_title', 'contacted', 'company', 'user_id', 'company_id']
        validators = [
            UniqueTogetherValidator(
                queryset=Employee.objects.all(),
                fields=['user_id', 'company_id', 'name'],
                message="Employee Already Exists"
            )
        ]