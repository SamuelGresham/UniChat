from django.db import models

# Create your models here.
class Subject (models.Model):
    subject_code = models.CharField(max_length=10, primary_key=True)

class Chat (models.Model):
    chat_name = models.CharField(max_length=100, default="")
    chat_platform = models.CharField(max_length=50)
    chat_link = models.CharField(max_length=100)
    course = models.CharField(max_length=100,default="")
    period = models.CharField(max_length=10, default="")
    approved = models.BooleanField(default=False)
    mess_id = models.CharField(max_length=20, default="")

class Request (models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    fb_link = models.CharField(max_length=100)
    mess_id = models.CharField(max_length=20, default="")
    added = models.BooleanField(default=False)


