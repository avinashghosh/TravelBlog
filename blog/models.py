from django.db import models

# Create your models here.

class Info(models.Model):
    Name = models.CharField(max_length=200)
    About = models.TextField(max_length=500)
    Insta = models.CharField(max_length=200)
    Whatsapp = models.CharField(max_length=200)
    Linkedin = models.CharField(max_length=200)

class Article(models.Model):
    Heading = models.CharField(max_length=200)
    Date = models.DateField()
    Brief = models.TextField(max_length=200)
    Desc = models.TextField(max_length=2000)
