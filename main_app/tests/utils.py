from faker import Faker
from main_app.models import *
from random import randint

faker = Faker()


def fake_user():
    user = User.objects.create(username=faker.first_name_male())
    return user


def fake_category():
    new_category = Category.objects.create(name=faker.word())
    return new_category


def fake_institution():
    new_institution = Institution.objects.create(
        name=faker.word(),
        description=faker.sentence(),
        type=randint(0, 2)
    )
    new_institution.categories.add(fake_category())
    return new_institution


def fake_donation():
    new_donation = Donation.objects.create(
        quantity=randint(1, 5),
        address=faker.address(),
        phone_number=randint(1000, 2000),
        city=faker.word(),
        zip_code="44-100",
        pick_up_date=faker.date(),
        pick_up_time=faker.time(),
        pick_up_comment=faker.sentence(),
        collected=True,
        user=fake_user()
    )
    new_donation.categories.add(fake_category())
    new_donation.institution.add(fake_institution())
    return new_donation
