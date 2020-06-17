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


# TESTS FOR EDIT MODELS:

@pytest.mark.django_db
def test_edit_user():
    # Given:
    user = fake_user()
    # When:
    previous_user_name = user.username
    user.username = "Charity"
    # Then:
    assert previous_user_name != user.username
    assert user.username == "Charity"


@pytest.mark.django_db
def test_edit_category():
    # Given:
    category = fake_category()
    # When:
    previous_category_name = category.name
    category.name = "Clothes"
    # Then:
    assert previous_category_name != category.name
    assert category.name == "Clothes"


@pytest.mark.django_db
def test_edit_institution():
    # Given:
    institution = fake_institution()
    # When:
    previous_institution_name = institution.name
    institution.name = "Fundacja"
    previous_institution_description = institution.description
    institution.description = "Some description"
    previous_institution_pk = institution.pk
    institution.pk = 2
    # Then:
    assert previous_institution_name != institution.name
    assert institution.name == "Fundacja"
    assert previous_institution_description != institution.description
    assert institution.description == "Some description"
    assert previous_institution_pk != institution.pk
    assert institution.pk == 2


@pytest.mark.django_db
def test_edit_donation():
    # Given:
    donation = fake_donation()
    # When:
    previous_donation_city = donation.city
    donation.city = "Katowice"
    previous_donation_date = donation.pick_up_date
    donation.pick_up_date = "2020-06-17"
    previous_donation_comment = donation.pick_up_comment
    donation.pick_up_comment = "Comment"
    previous_donation_status = donation.collected
    donation.collected = False
    # Then:
    assert previous_donation_city != donation.city
    assert donation.city == "Katowice"
    assert previous_donation_date != donation.pick_up_date
    assert donation.pick_up_date == "2020-06-17"
    assert previous_donation_comment != donation.pick_up_comment
    assert donation.pick_up_comment == "Comment"
    assert previous_donation_status != donation.collected
    assert donation.collected is False


# TESTS FOR DELETE MODELS:

@pytest.mark.django_db
def test_delete_user():
    # Given:
    user = fake_user()
    users_before_deletion = User.objects.count()
    # When:
    user.delete()
    # Then:
    assert User.objects.count() == users_before_deletion - 1


@pytest.mark.django_db
def test_delete_category():
    # Given:
    category = fake_category()
    categories_before_deletion = Category.objects.count()
    # When:
    category.delete()
    # Then:
    assert Category.objects.count() == categories_before_deletion - 1


@pytest.mark.django_db
def test_delete_institution():
    # Given:
    institution = fake_institution()
    institution_before_deletion = Institution.objects.count()
    # When:
    institution.delete()
    # Then:
    assert Institution.objects.count() == institution_before_deletion - 1


@pytest.mark.django_db
def test_delete_donation():
    # Given:
    donation = fake_donation()
    donation_before_deletion = Donation.objects.count()
    # When:
    donation.delete()
    # Then:
    assert Donation.objects.count() == donation_before_deletion - 1
