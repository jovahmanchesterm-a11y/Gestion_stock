# Create your views here.
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Fonksyon pou nou anrejistre yon itilizate nan system nan
def register(request):
    # Mesaj system
    if request.method == "POST":
        username = request.POST.get("username")
        email    = request.POST.get("email")
        password = request.POST.get("password") 
        confirm_password = request.POST.get("confirm_password")

        # Nap verifye si itilizate a egziste deja
        existing_user = User.objects.filter(email=email).first()

        # Verifye si itilizate a pa nil
        if existing_user is not None :
            print(f"existing user is : {existing_user}")
            # Mesaj Pou ki siyale itilizate a
            messages.info(request, "L'utilisateur existe deja !")
        else:
            print("L'utilisateur n'existe pas !")
            if password != confirm_password :
                print(f"Les mots de passe ne correspond pas !")
                # Mesaj Pou ki siyale itilizate a
                messages.info(request, "Les mot de passe ne correspond pas !")
            else :
                # Anrejistre itilizate a nan baz de done ah
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password
                )
                user.save()
                # Mesaj Pou ki siyale itilizate a 
                messages.success(request, "Utilisateur cree avec success !")
                return redirect("gestion_stock_app:index") 
    return render(request, './register.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        # Verifye si enfomasyon itilizata a korek
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(f"user autheticate  : {user}")
            login(request, user)
            messages.success(request, "Utilisateur connecte avec success !")
            return redirect("gestion_stock_app:index")
        else :
            messages.error(request, "Username and/or Password is incorrect !")
            print(f"user autheticate  : {user}")
    return render(request, './login.html')


# 
def logout_user(request):
    logout(request)
    return redirect("comptes:login")