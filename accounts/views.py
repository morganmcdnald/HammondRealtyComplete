from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User
from contacts.models import Contact
from likes.models import Like
from favourites.models import Favourite
from contactforms.models import Contactform
from comments.models import Comment

# Create your views here.
def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email is already in use')
                    return redirect('register')
                else:
                    # Validation passed, create user
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    messages.success(request, 'Registration Successful. You can now log in.')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in!')
            return redirect('account')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect ('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You have successfully logged out.')
        return redirect('index')

def account(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    user_likes = Like.objects.order_by('-id').filter(user_id=request.user.id)
    user_favourites = Favourite.objects.order_by('-id').filter(user_id=request.user.id)
    user_forms = Contactform.objects.order_by('-contact_date').filter(user_id=request.user.id)
    user_comments = Comment.objects.order_by('-comment_date').filter(user_id=request.user.id)
    context = {
        'contacts': user_contacts,
        'likes': user_likes,
        'favourites': user_favourites,
        'forms': user_forms,
        'comments': user_comments
    }
    return render(request, 'accounts/account.html', context)