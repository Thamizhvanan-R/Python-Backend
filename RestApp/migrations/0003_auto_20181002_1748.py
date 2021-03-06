# Generated by Django 2.0 on 2018-10-02 12:18

import RestApp.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RestApp', '0002_auto_20181002_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 2, 17, 48, 29, 913448)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Address',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='RestApp.address'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Avatar',
            field=models.ImageField(default=None, upload_to=RestApp.models.filename),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Phone',
            field=models.CharField(default=None, max_length=15),
        ),
        migrations.AlterField(
            model_name='profile',
            name='User',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
