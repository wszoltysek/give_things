from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.shortcuts import render, redirect
from django.views import View

from main_app.forms import *
from main_app.models import *


class Login(View):
    def get(self, request):
        form = LoginForm()
        ctx = {"form": form}
        return render(request, "user/login.html", ctx)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                error = "Brak takiego użytkownika lub błędne hasło."
                ctx = {"form": form, "error": error}
                return render(request, "user/login.html", ctx)


def logout_view(request):
    logout(request)
    return redirect("/")


class Register(View):
    def get(self, request):
        form = RegisterForm()
        ctx = {"form": form}
        return render(request, "user/register.html", ctx)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
        else:
            print(form.errors)
            ctx = {"form": form}
            return render(request, "user/register.html", ctx)


class LandingPage(View):
    def get(self, request):
        donation_count = Donation.objects. \
            values("quantity").annotate(the_count=Count("quantity"))
        institution_count = Donation.objects. \
            values("institution").annotate(the_count=Count("institution"))
        ctx = {
            "donation_count": donation_count,
            "institution_count": institution_count
        }
        return render(request, "index.html", ctx)


class AddDonation(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        categories = Category.objects.all()
        ctx = {"categories": categories}
        return render(request, "form.html", ctx)
