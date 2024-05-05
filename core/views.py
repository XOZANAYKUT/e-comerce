from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "index.html")


def profile(request):
     return render(request, "user/profile.html")



def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user_exists = User.objects.filter(email=email).exists()
        if user_exists:
            # User exists, check the password
            user = User.objects.get(email=email)
            if user.check_password(password):
                # User passed password verification, log in
                login(request, user)
                return redirect("index.html")
            else:
                # Password is incorrect, return error message
                return render(request, "user/login.html", {"error_message": "Password is incorrect"})
        else:
            # User not found, return error message
            return render(request, "user/login.html", {"error_message": "User not found"})
    else:
        # GET request, show the login page
        return render(request, "user/login.html")




def register(request):
     return render(request, "user/register.html")     


def logout(request):
    logout(request)
    return  HttpResponseRedirect(request.META.get('HTTP_REFERER', 'index'))

def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("/")
    return response    