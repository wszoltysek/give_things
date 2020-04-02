from django.core.mail import EmailMessage
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
        donations = Donation.objects.filter(user=request.user)\
            .order_by('collected', 'pick_up_date')
        ctx = {"donations": donations}
        return render(request, "user/panel.html", ctx)


class Settings(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        return render(request, "user/settings.html")

    def post(self, request):
        check = request.POST['password1']
        if request.user.check_password(check):
            user = User.objects.get(pk=request.user.id)
            if request.POST['first_name']:
                user.first_name = request.POST['first_name']
            if request.POST['last_name']:
                user.last_name = request.POST['last_name']
            if request.POST['email']:
                user.email = request.POST['email']
                user.username = request.POST['email']
            user.save()
            msg = "Poprawnie zmieniono dane."
            ctx = {'msg': msg}
            return render(request, "user/settings.html", ctx)
        msg = "Błędne hasło!"
        ctx = {"msg": msg}
        return render(request, "user/settings.html", ctx)


class PasswordChange(LoginRequiredMixin, View):
    login_url = '/login/'

    def post(self, request):
        check = request.POST['password2']
        if request.user.check_password(check):
            user = User.objects.get(pk=request.user.id)
            if request.POST['new_password'] == request.POST['new_password2']:
                user.set_password(request.POST['new_password'])
                user.save()
            return redirect("/")
        msg = "Błędne hasło."
        ctx = {"msg": msg}
        return render(request, "user/settings.html", ctx)


class ChangeStatus(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request, id):
        status = Donation.objects.get(pk=id)
        if status.collected:
            status.collected = False
        else:
            status.collected = True
        status.save()
        return redirect("panel")


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
        return render(request, "index.html", ctx)


class AddDonation(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        categories = Category.objects.all()
        institutions = Institution.objects.all()
        ctx = {
            "categories": categories,
            "institutions": institutions
        }
        return render(request, "form.html", ctx)

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
            user=request.user
        )
        for category_name in categories:
            new_donation.categories.add(Category.objects.get(name=category_name))
        new_donation.institution.add(Institution.objects.get(name=request.POST.get('institution')))
        new_donation.save()
        return redirect("confirmation")


class Confirmation(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        return render(request, "form-confirmation.html")


class ContactForm(View):
    def post(self, request):
        message = request.POST['message']
        admins = User.objects.filter(is_superuser=True)
        mails = [admin.email for admin in admins if len(admin.email) > 3]
        subject = f'Kontakt od {request.POST["name"]} {request.POST["surname"]}'
        email = EmailMessage(subject, message, to=mails)
        email.send()
        return redirect("success")


class ContactSuccess(View):
    def get(self, request):
        return render(request, "contact-success.html")
