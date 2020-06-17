import pytest
from main_app.models import *
from main_app.tests.utils import *


# TESTS FOR CREATE MODELS:

@pytest.mark.django_db
def test_create_user():
    # Given:
    users_before = User.objects.count()
    # When:
    new_user = fake_user()
    # Then:
    assert User.objects.count() == users_before + 1
    assert new_user.pk == 1
    assert new_user.is_anonymous is False


@pytest.mark.django_db
def test_create_category():
    # Given:
    categories_before = Category.objects.count()
    # When:
    new_category = fake_category()
    # Then:
    assert Category.objects.count() == categories_before + 1
    assert Category.objects.count() == 1
    assert new_category.pk == 1


@pytest.mark.django_db
def test_create_institution():
    # Given:
    institutions_before = Institution.objects.count()
    # When:
    new_institution = fake_institution()
    # Then:
    assert Institution.objects.count() == institutions_before + 1
    assert Institution.objects.count() == 1
    assert new_institution.pk == 1


@pytest.mark.django_db
def test_create_donation():
    # Given:
    donations_before = Donation.objects.count()
    # When:
    new_donation = fake_donation()
    # Then:
    assert Donation.objects.count() == donations_before + 1
    assert Donation.objects.count() == 1
    assert new_donation.pk == 1
