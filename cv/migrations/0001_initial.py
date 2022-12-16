# Generated by Django 4.1.1 on 2022-12-14 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
                ('tasks', models.TextField()),
                ('beginDate', models.IntegerField()),
                ('endDate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=20)),
                ('skillType', models.CharField(choices=[('linguistic', 'linguistic'), ('technical', 'technical')], max_length=20)),
                ('levelPercent', models.IntegerField()),
                ('skillIcon', models.ImageField(default='icon.png', upload_to='skillsIcons/')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=100)),
                ('beginDate', models.IntegerField()),
                ('endDate', models.IntegerField()),
                ('location', models.CharField(max_length=50)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cv.type')),
            ],
        ),
    ]