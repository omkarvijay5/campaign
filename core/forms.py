# python imports

# django imports
from django import forms

# third party imports
from core.models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'
