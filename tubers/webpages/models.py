from django.db import models
from django.db.models.base import Model

# Create your models here.
class TopSlider(models.Model):
    headline = models.CharField(max_length=250)
    subtitile = models.CharField(max_length=250)
    button_Text = models.CharField(max_length=250)
    url = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='media/slider/%Y/%m')
    created_date = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.headline 

class Team(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    fb_link = models.CharField(max_length=255)
    insta_link = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/team/%Y/%m/%d/')
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.firstName} {self.lastName}'


