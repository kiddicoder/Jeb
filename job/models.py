from django.contrib.auth.models import User
from django.db import models
from company.models import Company


class JobCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Job(models.Model):
    EMPLOYMENT_TYPES = [
        ('FT', 'Full-time'),
        ('PT', 'Part-time'),
    ]
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=9999, blank=True)
    category = models.ForeignKey(JobCategory, on_delete=models.CASCADE)
    employment_type = models.CharField(max_length=2, choices=EMPLOYMENT_TYPES)
    location = models.CharField(max_length=255, blank=True)
    start_date = models.DateField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class FavoriteJob(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_jobs')
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='favorited_by')

    def __str__(self):
        return f"{self.user.username} favorited {self.job.title}"
