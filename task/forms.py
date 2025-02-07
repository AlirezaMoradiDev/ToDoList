from django import forms
from task.models import Task


class TaskForm(forms.ModelForm):
    user = forms.CharField()

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user:
            self.user.initial = user.username

    class Meta:
        model = Task
        fields = ['title', 'description']

    level_priority = [
        ('low', 'LOW'),
        ('medium', 'MEDIUM'),
        ('high', 'HIGH')
    ]

    priority = forms.ChoiceField(widget=forms.RadioSelect(), choices=level_priority)
