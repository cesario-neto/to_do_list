from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'task_text', 'end_in', 'status']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título',
            }),
            'task_text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Resumo',
            }),
            'end_in': forms.HiddenInput(),
            'status': forms.Select(attrs={
                'class': 'form-select',
            }),
        }
