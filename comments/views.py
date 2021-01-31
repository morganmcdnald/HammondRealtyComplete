from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Comment

# Create your views here.
def comment(request):
    if request.method == 'POST':
        blog = request.POST['blog']
        blog_id = request.POST['blog_id']
        username = request.POST['username']
        comment = request.POST['comment']
        user_id = request.POST['user_id']

        comment = Comment(blog=blog, blog_id=blog_id, username=username, comment=comment, user_id=user_id)
        comment.save()

        messages.success(request, 'Your comment was posted successfully.')
        return redirect('/blogs/'+blog_id)