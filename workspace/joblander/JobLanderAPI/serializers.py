from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User, Group
from rest_framework.validators import UniqueTogetherValidator, UniqueValidator


class CompanySerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        validators=[UniqueValidator(queryset=Company.objects.all(), message="Company Already Exists")]
    )
    class Meta:
        model = Company
        fields = '__all__'

class EmployeesSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        validators=[UniqueValidator(queryset=Employee.objects.all(), message="Employee Already Exists")]
    )
    class Meta:
        model = Employee
        fields = '__all__'