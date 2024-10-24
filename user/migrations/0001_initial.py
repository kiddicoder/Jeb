# Generated by Django 5.0.6 on 2024-05-17 11:08

import django.db.models.deletion
import django_countries.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('job_application', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pictures/')),
                ('bio', models.TextField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='user_files/')),
                ('from_profile', models.BooleanField(default=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='user.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=255)),
                ('company_name', models.CharField(max_length=255)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('from_profile', models.BooleanField(default=True)),
                ('job_application', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='experiences', to='job_application.jobapplication')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiences', to='user.profile')),
            ],
        ),
        migrations.CreateModel(
            name='ContactInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('phone_number', models.CharField(max_length=20)),
                ('street_name', models.CharField(max_length=255)),
                ('house_number', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=255)),
                ('postal_code', models.CharField(max_length=20)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('from_profile', models.BooleanField(default=False)),
                ('job_application', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contact_information', to='job_application.jobapplication')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_information', to='user.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('can_be_contacted', models.BooleanField()),
                ('from_profile', models.BooleanField(default=True)),
                ('job_application', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='references', to='job_application.jobapplication')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='references', to='user.profile')),
            ],
        ),
    ]
