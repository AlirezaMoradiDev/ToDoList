from django import forms
from task.models import Task


class TaskForm(forms.ModelForm):
    level_priority = [
        ('low', 'LOW'),
        ('medium', 'MEDIUM'),
        ('high', 'HIGH')
    ]
    priority = forms.ChoiceField(widget=forms.RadioSelect(), choices=level_priority)

    class Meta:
        model = Task
        fields = ['priority', 'title', 'description', 'image']

        widgets = {
            'description': forms.TextInput()
        }


class EditForm(forms.ModelForm):

    level_priority = [
        ('low', 'LOW'),
        ('medium', 'MEDIUM'),
        ('high', 'HIGH')
    ]
    priority = forms.ChoiceField(widget=forms.RadioSelect(), choices=level_priority)

    class Meta:
        model = Task
        fields = ['priority', 'title', 'description']
        widgets = {
            'description': forms.TextInput()
        }
