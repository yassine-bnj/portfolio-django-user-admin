# Generated by Django 4.1.1 on 2022-12-15 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0002_remove_type_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='skillIcon',
            field=models.ImageField(default='icon.png', upload_to='cv/static/skillsIcons/'),
        ),
    ]