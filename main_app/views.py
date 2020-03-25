from django.db.models import Count
from django.shortcuts import render, redirect
from django.views import View

from main_app.forms import *
from main_app.models import *


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


class Login(View):
    def get(self, request):
        return render(request, "user/login.html")


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


class AddDonation(View):
    def get(self, request):
        return render(request, "form.html")
