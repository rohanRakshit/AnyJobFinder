from django.db import models

# Create your models here.

class frontInfo(models.Model):
    label=models.AutoField
    thumbnail = models.ImageField(upload_to='static/AJF')
    title = models.CharField(max_length=20)
    shortDesc = models.CharField(max_length=100)
    link = models.URLField(max_length=777)

    def __str__(self):
        return self.title

class detail(models.Model):
    thumbnail = models.ImageField(upload_to='static/AJF')
    title = models.CharField(max_length=30)
    Desc = models.TextField(max_length=10000)
    link = models.URLField(max_length=777)

    def __str__(self):
        return self.title