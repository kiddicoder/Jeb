from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from job.models import Job


class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('in_progress', 'In Progress'),
        ('submitted', 'Submitted'),
        ('reviewed', 'Reviewed'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_applications')
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    submitted_at = models.DateTimeField(null=True, blank=True)
    is_submitted = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_progress')
    cover_letter = models.TextField(blank=True)

    def __str__(self):
        return f"Application by {self.user.username} for {self.job.title}"

    def submit(self):
        self.is_submitted = True
        self.submitted_at = timezone.now()
        self.status = 'submitted'
        self.save()

