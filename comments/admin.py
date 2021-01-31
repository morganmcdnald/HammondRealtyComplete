from django.contrib import admin
from .models import Comment

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'blog_id', 'comment_date')
    list_display_links = ('id', 'username', 'blog_id')
    search_fields = ('username', 'blog_id', 'comment_date')
    list_per_page = 25

admin.site.register(Comment, CommentAdmin)