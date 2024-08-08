from django.db import models


# Create your models here.
class contact(models.Model):
    help=models.CharField(max_length=200)
    industry=models.CharField(max_length=200)
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    phone=models.CharField(max_length=12)
    email=models.EmailField()
    company=models.CharField(max_length=200)
    message=models.CharField(max_length=2000)
    def __str__(self):
        return self.first_name



