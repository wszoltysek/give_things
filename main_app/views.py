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


class UserPanel(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        return render(request, "user/panel.html")


class LandingPage(View):
    def get(self, request):
        donations = Donation.objects.all()
        institutions_donated = Institution.objects.filter(donation__quantity__gt=0).count()
        all_institutions = Institution.objects.all()
        bags_qty = 0
        for bags in donations:
            bags_qty += bags.quantity
        ctx = {
            'bags_qty': bags_qty,
            'institutions_donated': institutions_donated,
            'all_institutions': all_institutions
        }
        return render(request, 'index.html', ctx)


class AddDonation(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        categories = Category.objects.all()
        institutions = Institution.objects.all()
        donations = DonationForm()
        ctx = {
            "categories": categories,
            "institutions": institutions,
            "donations": donations
        }
        return render(request, "form.html", ctx)


class Confirmation(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        return render(request, "form-confirmation.html")
