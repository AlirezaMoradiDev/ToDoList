from django import forms
from .models import Ticket
from django.forms import ValidationError


class AddTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise ValidationError('Title is required.')
        else:
            return title

