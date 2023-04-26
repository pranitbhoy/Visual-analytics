from django.db import models

# Create your models here.
class USER_details(models.Model):
    password= models.CharField(max_length=20)
    email_id= models.CharField(max_length=20)