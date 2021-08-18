from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.
class Youtuber(models.Model):
    crew_choices =(
        ('Solo', 'Solo'),
        ('Small', 'Small'),
        ('Large', 'Large'),
    )

    camera_choices = (
        ('Canon', 'Canon'),
        ('Nikon', 'Nikon'),
        ('Sony', 'Sony'),
        ('Red', 'Red'),
        ('Fuji', 'Fuji'),
        ('Panasonic', 'Panasonic'),
        ('Other', 'Other')
    )

    category_choices = (
        ('Code', 'Code'),
        ('Mobile review', 'Mobile review'),
        ('Comedy', 'Comedy'),
        ('Vlogs', 'Vlogs'),
        ('Gaming', 'Gaming'),   
        ('Cooking', 'Cooking'),
        ('Other', 'Other')
    )
    
    name = models.CharField(max_length=255, null=False)
    price = models.IntegerField(null=False)
    photo = models.ImageField(upload_to='media/ytubers/%Y/%m')
    video_url = models.CharField(max_length=255)
    description = RichTextField()
    city = models.CharField(max_length=255, null=False)
    age = models.IntegerField()
    height = models.IntegerField(null=False)
    crew = models.CharField(choices=crew_choices, max_length=255)
    camera_type = models.CharField(choices=camera_choices, max_length=255, null=False)
    subs_count = models.IntegerField(null=False)
    category = models.CharField(choices=category_choices,  max_length=255, null=False)
    is_featured = models.BooleanField(default= False)
    created_date = models.DateTimeField(default= datetime.now, blank=True)

    def __str__(self):
        return self.name
    
