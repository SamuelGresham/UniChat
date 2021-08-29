from django.db import models

# Create your models here.
class Subject (models.Model):
    subject_code = models.CharField(max_length=10, primary_key=True)
    subject_name = models.CharField(max_length=50)
    faculty_name = models.CharField(max_length=50)

class Chat (models.Model):
    chat_platform = models.CharField(max_length=50)
    chat_link = models.CharField(max_length=100)
