from django.db import models

# Create your models here.
class Event(models.Model):
    event_title=models.CharField(max_length=120)
    location=models.CharField(max_length=100)
    date =models.CharField(max_length=100)
    description=models.TextField()
    
    def __str__(self):
        return self.event_title

class Applicant(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.IntegerField()
    event=models.ForeignKey('Event',on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name
