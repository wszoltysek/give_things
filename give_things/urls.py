"""give_things URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPage.as_view(), name="index"),
    path('contact/', ContactForm.as_view(), name="contact"),
    path('success/', ContactSuccess.as_view(), name="success"),

    path('login/', Login.as_view(), name="login"),
    path('logout/', logout_view, name="logout"),
    path('register/', Register.as_view(), name="register"),
    path('panel/', UserPanel.as_view(), name="panel"),
    path('settings/', Settings.as_view(), name="settings"),
    path('password/', PasswordChange.as_view(), name="password_change"),

    path('add/', AddDonation.as_view(), name="add"),
    path('change/<int:id>/', ChangeStatus.as_view(), name="status"),
    path('confirmation/', Confirmation.as_view(), name="confirmation")
]
