from django.contrib.auth.models import User
from django.db import models
from django_countries.fields import CountryField

from job_application.models import JobApplication


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    bio = models.TextField(blank=True)


class ContactInformation(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='contact_information')
    job_application = models.ForeignKey(JobApplication, on_delete=models.CASCADE, related_name='contact_information', null=True, blank=True)
    full_name = models.CharField(max_length=255)
    birthdate = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=20)
    street_name = models.CharField(max_length=255)
    house_number = models.CharField(max_length=20)
    city = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20)
    country = CountryField()
    from_profile = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name


class Experience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='experiences')
    job_application = models.ForeignKey(JobApplication, on_delete=models.CASCADE, related_name='experiences', null=True, blank=True)
    role = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    from_profile = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.role} at {self.company_name}"


class Reference(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='references')
    job_application = models.ForeignKey(JobApplication, on_delete=models.CASCADE, related_name='references', null=True, blank=True)
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    can_be_contacted = models.BooleanField()
    from_profile = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.role}"

