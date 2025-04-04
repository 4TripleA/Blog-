from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [  
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("master/", views.master, name="master"), 
    path("profile/<str:username>/", views.profile, name="profile"),
    path("newnews/", views.newnews, name="newnews"), 
    path("editprofile/", views.editprofile, name="editprofile"),
    path("logout/", views.logout, name="logout"), 
]   