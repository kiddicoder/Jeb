from django import forms
from job.models import Job
from utilities.widgets import QuillEditorWidget


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'category', 'employment_type', 'start_date', 'due_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control custom-input'}),
            'description': QuillEditorWidget(attrs={'class': 'form-control custom-input'}, options={'theme': 'snow', 'placeholder': 'Enter the job description'}),
            'category': forms.Select(attrs={'class': 'form-control custom-input'}),
            'employment_type': forms.Select(attrs={'class': 'form-control custom-input'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control custom-input', 'type': 'date'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control custom-input', 'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        due_date = cleaned_data.get("due_date")

        if not start_date:
            self.add_error('start_date', 'Start date is required.')
        if not due_date:
            self.add_error('due_date', 'Due date is required.')

        return cleaned_data