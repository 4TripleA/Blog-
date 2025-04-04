from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from register.forms import adduserform
from django.contrib import messages
from register.models import blogpost, profilepage
from django.contrib.auth.decorators import login_required
from register.forms import newblogform, editprofileform
import jwt, datetime

 
# Create your views here.
posts = [ 
    {
        'author': '4Triple',
        'title': 'Blogs',
        'content': 'finished day',
        'date_posted': '8th september, 2024',
    }
    
]  
 
@login_required
def home(request):
    return render(request, "home.html", {'posts': blogpost.objects.all().order_by('-date_posted')})


def master(request):
    return render(request, "master.html", {})

def register(request):
    submitted = False
    if request.method == "POST":

        form = adduserform(request.POST)
        if form.is_valid():
            form.save()
             
            messages.success(request, 'Registration Successful')

            return redirect('login')
    else:
        form = adduserform
        if 'submitted' in request.GET:
            submitted = True 

    payload = {
        'id': request.user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        'iat': datetime.datetime.utcnow(),
    } 

    token = jwt.encode(payload, 'secret', algorithm='HS256').encode('utf-8')
    
    return render(request, "Register.html", {'form':form, 'submitted':submitted})
 
def profile(request, username):
    user = get_object_or_404(User, username=username)
    profiles = profilepage(user=user)
    return render(request, "profilepage.html", {'profiles': profiles})

def newnews(request):
    author = request.user.id
    if request.method == 'POST':
        form = newblogform(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')

            p, created = blogpost.objects.get_or_create(title=title, content=content, author_id=author)
            p.save()

            return redirect("/") 
        
    else:
        form = newblogform()  

    return render(request, "newnews.html", {'form':form})

def editprofile(request):
    user = request.user.id
    if request.method == "POST":
        form = editprofileform(request.POST)
        if form.is_valid():
            bio = form.cleaned_data.get('bio')
            location = form.cleaned_data.get('location')

            q, created = profilepage.objects.get_or_create(bio=bio, location=location, user=User)
            q.save()

            return redirect("/")
    else:
        form = editprofileform()

    return render(request, "editprofile.html", {'form': form})

def logout(request):
    return render(request, "registration/logout.html", {})



