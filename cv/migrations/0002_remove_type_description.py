# Generated by Django 4.1.1 on 2022-12-14 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='type',
            name='description',
        ),
    ]