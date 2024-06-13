from django.db import models
#testowy model
class Games(models.Model):
    category = models.CharField(max_length = 255)
    name = models.CharField(max_length = 255)
    price = models.FloatField()
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
#aktualny model
class lol(models.Model):
    category = models.CharField(max_length = 255)
    name = models.CharField(max_length = 255)
    price = models.FloatField()
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')












