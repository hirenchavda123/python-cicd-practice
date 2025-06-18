from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def landing_page_view(request):
    return render(request, "landingpage.html")


def login_view(request):
    if request.method == "POST":
        data = request.POST
        username = data.get("username")
        password = data.get("password")
        user = User.objects.filter(username=username)
        if not user:
            messages.error(request, f"Username:{username} does not exists.")
            return render(request, "login.html")
        if not check_password(password, user[0].password):
            messages.error(request, "Password is incorrect.")
            return render(request, "login.html")
        context = {"message": f"User with username:{username} logged in successfully."}
        return render(request, "home.html", context=context)
    return render(request, "login.html")


def signup_view(request):
    if request.method == "POST":
        try:
            print('try: ===>>')
        except:
            print('except: ==>>')
        data = request.POST
        email = data.get("email")
        username = data.get("username")
        password = data.get("password")
        check_username = User.objects.filter(username=username).exists()
        if check_username:
            messages.error(
                request,
                f"User with username:{username} already exists. Try another username.",
            )
            return render(request, "signup.html")
        check_email = User.objects.filter(email=email).exists()
        if check_email:
            messages.error(
                request, f"User with email:{email} already exists. Try another email."
            )
            return render(request, "signup.html")
        User.objects.create(
            username=username, email=email, password=make_password(password)
        )
        context = {"message": f"User with username:{username} created successfully."}
        return render(request, "login.html", context=context)
    return render(request, "signup.html")


@login_required(login_url="/login/")
def home_view(request):
    return render(request, "home.html")
