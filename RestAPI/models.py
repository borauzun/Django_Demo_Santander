from django.db import models

# Create your models here.
class APIKey(models.Model):
    keyId= models.AutoField(primary_key=True) 
    apiKey=models.CharField(max_length=100, blank=True)
    name=models.CharField(max_length=100, blank=True)

class TodoItem(models.Model):
    todoId= models.AutoField(primary_key=True) 
    name=models.CharField(max_length=100, blank=True)
    lastName=models.CharField(max_length=100, blank=True)