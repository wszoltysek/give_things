# Generated by Django 2.2.7 on 2020-03-31 09:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20200325_1201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation',
            name='institution',
        ),
        migrations.AddField(
            model_name='donation',
            name='institution',
            field=models.ManyToManyField(to='main_app.Institution'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]