# Generated by Django 2.2.7 on 2020-03-31 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_auto_20200331_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='collected',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
