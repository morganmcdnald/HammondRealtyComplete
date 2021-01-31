from django.db import models

# Create your models here.
class Like(models.Model):
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=200)
    user_id = models.IntegerField(blank=True)
    def __str__(self):
        return self.listing