from django import forms
from django.forms import ModelForm, widgets
from django_countries.widgets import CountrySelectWidget

from user.models import Profile, ContactInformation, Experience, Reference


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        widgets = {
            'profile_picture': widgets.ClearableFileInput(attrs={'class': 'form-control'}),
            'bio': widgets.Textarea(attrs={'class': 'form-control'}),
        }


class ProfilePictureForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture']
        widgets = {
            'profile_picture': widgets.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class ContactInformationForm(forms.ModelForm):
    class Meta:
        model = ContactInformation
        exclude = ['profile', 'job_application', 'from_profile']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control custom-input'}),
            'birthdate': forms.DateInput(attrs={'class': 'form-control custom-input', 'type': 'date'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control custom-input'}),
            'street_name': forms.TextInput(attrs={'class': 'form-control custom-input'}),
            'house_number': forms.TextInput(attrs={'class': 'form-control custom-input'}),
            'city': forms.TextInput(attrs={'class': 'form-control custom-input'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control custom-input'}),
            'country': CountrySelectWidget(attrs={'class': 'form-control custom-input'}),
        }


class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        exclude = ['profile', 'job_application', 'from_profile']
        widgets = {
            'role': widgets.TextInput(attrs={'class': 'form-control custom-input'}),
            'company_name': widgets.TextInput(attrs={'class': 'form-control custom-input'}),
            'start_date': widgets.DateInput(attrs={'class': 'form-control custom-input', 'type': 'date'}),
            'end_date': widgets.DateInput(attrs={'class': 'form-control custom-input', 'type': 'date'}),
        }

    def clean_start_date(self):
        start_date = self.cleaned_data.get('start_date')
        if not start_date:
            raise forms.ValidationError('This field is required.')
        return start_date

    def clean_end_date(self):
        end_date = self.cleaned_data.get('end_date')
        if not end_date:
            raise forms.ValidationError('This field is required.')
        return end_date
class ReferenceForm(ModelForm):
    class Meta:
        model = Reference
        exclude = ['profile', 'job_application', 'from_profile']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control custom-input'}),
            'role': widgets.TextInput(attrs={'class': 'form-control custom-input'}),
            'email': widgets.EmailInput(attrs={'class': 'form-control custom-input'}),
            'phone_number': widgets.TextInput(attrs={'class': 'form-control custom-input'}),
            'can_be_contacted': widgets.CheckboxInput(attrs={'class': 'form-check-input custom-checkbox'}),
        }
