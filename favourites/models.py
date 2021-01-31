from django.db import models

# Create your models here.
class Favourite(models.Model):
    blog = models.CharField(max_length=200)
    blog_id = models.IntegerField()
    username = models.CharField(max_length=200)
    user_id = models.IntegerField()
    def __str__(self):
        return self.blog