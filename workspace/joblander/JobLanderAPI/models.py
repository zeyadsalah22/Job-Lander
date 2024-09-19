from django.db import models
from enum import Enum
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    careers_link = models.URLField(null=True)
    linkedin_link = models.URLField(null=True)
    def __str__(self):
        return f"Company: {self.name}"
    
class ContactStatus(Enum):
    SENT = 'Sent'
    ACCEPTED = 'Accepted'
    MESSAGED = 'Messaged'
    REPLIED = 'Replied'
    STRONG_CONNECTION = 'Established Connection'

class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    linkedin_link = models.URLField(blank=True)
    email = models.EmailField(null=True, blank=True)
    job_title = models.CharField(max_length=255)
    contacted = models.CharField(max_length=255, choices=[(tag.name, tag.value) for tag in ContactStatus])
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.job_title}: {self.name} works in {self.company.name}"

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    question = models.TextField()
    answer = models.TextField()
    application = models.ForeignKey('Application', on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"Question: {self.question}"

class ApplicationStatus(Enum):
    PENDING = 'Pending'
    ASSESSMENT = 'Assessment'
    INTERVIEW = 'Interview'
    REJECTED = 'Rejected'
    ACCEPTED = 'Accepted'

class Stage(Enum):
    APPLIED = 'Applied'
    PHONE_SCREEN = 'Phone Screen'
    ASSESSMENT = 'Assessment'
    INTERVIEW = 'Interview'
    OFFER = 'Offer'

class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    job_title = models.CharField(max_length=255)
    job_type = models.CharField(max_length=255)
    description = models.TextField()
    link = models.CharField(max_length=255)
    submitted_cv = models.FileField(null=True)
    ats_score = models.SmallIntegerField(default=0)
    stage = models.CharField(max_length=255, choices=[(tag.name, tag.value) for tag in Stage])
    status = models.CharField(max_length=255, choices=[(tag.name, tag.value) for tag in ApplicationStatus])
    submission_date = models.DateField(auto_now_add=True)
    contacted_employees = models.ManyToManyField(Employee)

    def __str__(self):
        return f"{self.job_title} at {self.company.name} is {self.status}"


