from django.db.models import Count
from django.shortcuts import render
from django.views import View

from main_app.models import *


class LandingPage(View):
    def get(self, request):
        donation_count = Donation.objects.\
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
        return render(request, "user/register.html")


class AddDonation(View):
    def get(self, request):
        return render(request, "form.html")
