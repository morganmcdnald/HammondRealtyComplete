from django.contrib import admin
from .models import Like

# Register your models here.
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listing')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'listing')
    list_per_page = 25

admin.site.register(Like, LikeAdmin)