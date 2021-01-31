from django.shortcuts import render, get_object_or_404
from .models import Blog
from comments.models import Comment
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import category_choices, author_choices

# Create your views here.
def index(request):
    blogs = Blog.objects.order_by('-post_date').filter(is_published=True)
    paginator = Paginator(blogs, 6)
    page = request.GET.get('page')
    paged_blogs = paginator.get_page(page)

    context = {
        'blogs': paged_blogs,
        'category_choices': category_choices,
        'author_choices': author_choices
    }
    return render(request, 'blogs/blogs.html', context)

def blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    comments = Comment.objects.order_by('-comment_date').filter(blog_id=blog_id)
    context = {
        'blog': blog,
        'comments': comments
    }
    return render(request, 'blogs/blog.html', context)

def search(request):
    queryset_list = Blog.objects.order_by('-post_date').filter(is_published=True)

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(content__icontains=keywords)

    # Type
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            queryset_list = queryset_list.filter(category__iexact=category)

    # Author
    if 'author' in request.GET:
        author = request.GET['author']
        if author:
            queryset_list = queryset_list.filter(author__name__iexact=author)

    context = {
        'category_choices': category_choices,
        'author_choices': author_choices,
        'blogs': queryset_list,
        'values': request.GET
    }
    return render(request, 'blogs/blogSearch.html', context)