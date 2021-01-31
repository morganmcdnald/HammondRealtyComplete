from django.contrib import admin
from .models import Blog

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'category', 'is_published', 'post_date')
    list_display_links = ('id', 'title')
    list_filter = ('author', 'category')
    list_editable = ('is_published',)
    search_fields = ('title',)
    list_per_page = 25

admin.site.register(Blog, BlogAdmin)