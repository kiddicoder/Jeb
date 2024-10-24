from django.forms import ModelForm
from django import forms

from job_application.models import JobApplication


class CoverLetterForm(ModelForm):
    class Meta:
        model = JobApplication
        fields = ['cover_letter']
        widgets = {
            'cover_letter': forms.Textarea(attrs={'class': 'form-control custom-input custom-textbox', 'rows': 10}),
        }
