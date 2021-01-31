from django.db import models
from datetime import datetime
from realtors.models import Realtor

# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=300, blank=True)
    category = models.CharField(max_length=200)
    content = models.TextField()
    blog_photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    post_date = models.DateField(default=datetime.now, blank=True)
    def __str__(self): 
        return self.title