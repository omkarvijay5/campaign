# python imports

# django imports
from django import forms
from django.contrib.auth.models import User

# third party imports
from core.models import Contact, Campaign


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email',)


class CampaignForm(forms.ModelForm):

    contacts = forms.ModelMultipleChoiceField(
        queryset=Contact.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Campaign
        fields = ('title', 'from_date', 'to_date', 'is_active', 'content', 'contacts')
