from django.db import models

# Create your models here.
class USER_details(models.Model):
    firstname=models.CharField(max_length=30)
    lastname= models.CharField(max_length=20)
    email_id= models.CharField(max_length=20)


