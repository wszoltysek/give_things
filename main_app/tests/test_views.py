import pytest
from django.test import Client
from main_app.tests.utils import *

client = Client()


# USERS VIEWS:

def test_view_register_get():
    response = client.get("/register/")
    assert response.status_code == 200


def test_view_register_post():
    response = client.post("/register/")
    assert response.status_code == 200


def test_view_login_get():
    response = client.get("/login/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_view_login_post():
    response = client.post("/login/", {"username": "user@email.com", "password": "pass01#"})
    assert response.status_code == 200


def test_view_logout_get():
    response = client.get("/logout/")
    assert response.status_code == 302


def test_view_logout_post():
    response = client.post("/logout/")
    assert response.status_code == 302


def test_view_user_panel_get():
    response = client.get("/panel/")
    assert response.status_code == 302


def test_view_user_settings_get():
    response = client.get("/settings/")
    assert response.status_code == 302


def test_view_user_settings_post():
    response = client.post("/settings/")
    assert response.status_code == 302


def test_view_user_password_change_get():
    response = client.get("/password/")
    assert response.status_code == 302


def test_view_user_password_change_post():
    response = client.post("/password/")
    assert response.status_code == 302


# MAIN VIEWS:

@pytest.mark.django_db
def test_view_landing_page_get():
    response = client.get("/")
    assert response.status_code == 200


def test_view_admin_get():
    response = client.get("/admin/")
    assert response.status_code == 302


@pytest.mark.django_db
def test_view_contact_post():
    response = client.post("/contact/", {
        "message": "some message",
        "name": "Mark",
        "surname": "Kowalski"
    })
    assert response.status_code == 302


def test_view_contact_success_get():
    response = client.get("/success/")
    assert response.status_code == 200


# DONATION VIEWS:

def test_view_add_donation_get():
    response = client.get("/add/")
    assert response.status_code == 302


def test_view_add_donation_post():
    response = client.post("/add/")
    assert response.status_code == 302


def test_view_donation_confirmation_get():
    response = client.get("/confirmation/")
    assert response.status_code == 302


@pytest.mark.django_db
def test_view_donation_change_status_get():
    donation = fake_donation()
    response = client.get(f"/change/{donation.pk}/")
    assert response.status_code == 302


@pytest.mark.django_db
def test_view_donation_change_status_post():
    donation = fake_donation()
    response = client.post(f"/change/{donation.pk}/")
    assert response.status_code == 302
