from utilities.widgets import QuillEditorWidget
from django import forms
from django.forms import ModelForm, widgets
from company.models import Company

class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'description', 'address', 'logo', 'cover_image']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control custom-input'}),
            'description': QuillEditorWidget(attrs={'class': 'form-control custom-input'}, options={'theme': 'snow', 'placeholder': 'Enter the company description'}),
            'address': widgets.TextInput(attrs={'class': 'form-control custom-input'}),
            'logo': widgets.ClearableFileInput(attrs={'class': 'form-control custom-input'}),
            'cover_image': widgets.ClearableFileInput(attrs={'class': 'form-control custom-input'}),
        }

    def clean_logo(self):
        logo = self.cleaned_data.get('logo')
        if not logo:
            raise forms.ValidationError('This field is required.')
        return logo

    def clean_cover_image(self):
        cover_image = self.cleaned_data.get('cover_image')
        if not cover_image:
            raise forms.ValidationError('This field is required.')
        return cover_image
