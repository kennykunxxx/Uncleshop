# Generated by Django 3.0.5 on 2020-04-27 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20200427_1704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qanda',
            name='email',
        ),
    ]