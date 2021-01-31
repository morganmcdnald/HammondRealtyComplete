from django.db import models
from datetime import datetime

# Create your models here.
class Comment(models.Model):
    blog = models.CharField(max_length=200)
    blog_id = models.IntegerField()
    username = models.CharField(max_length=200)
    comment = models.TextField()
    comment_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)
    def __str__(self):
        return self.username