from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from main_app.forms import *
from main_app.models import *


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


class UserPanel(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        donations = Donation.objects.filter(user=request.user).order_by('pick_up_date').order_by('collected')
        ctx = {"donations": donations,}
        return render(request, "user/panel.html", ctx)


class ChangeStatus(View):
    def get(self, request, id):
        status = Donation.objects.get(pk=id)
        if status.collected:
            status.collected = False
        else:
            status.collected = True
        status.save()
        return redirect('/panel/')


def logout_view(request):
    logout(request)
    return redirect("/")


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
        return render(request, 'form.html', {'categories': categories,
                                             'institutions': institutions})

    def post(self, request):
        categories = request.POST.get('categories-choose').split(',')
        new_donation = Donation.objects.create(
            quantity=request.POST.get('bags'),
            address=request.POST.get('address'),
            city=request.POST.get('city'),
            zip_code=request.POST.get('zip_code'),
            phone_number=request.POST.get('phone'),
            pick_up_date=request.POST.get('date'),
            pick_up_time=request.POST.get('time'),
            pick_up_comment=request.POST.get('more_info'),
            user_id=request.user.pk
        )
        for category_name in categories:
            new_donation.categories.add(Category.objects.get(name=category_name))
            new_donation.save()
        new_donation.institution.add(Institution.objects.get(name=request.POST.get('institution')).pk)
        new_donation.save()
        return redirect('/confirmation/')


class Confirmation(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        return render(request, "form-confirmation.html")
