# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# python imports

# django imports
from django.shortcuts import render
from django.views.generic import View
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect

# third party imports
from core.forms import ContactForm, UserForm, CampaignForm


class Dashboard(View):
    """
    Dashboard is the main dashboard of the campaign
    Dashboard has multiple forms which enables to create a campaign
    """
    template_name = 'core/dashboard.html'

    def get(self, request, *args, **kwargs):
        user_form_class = UserForm(prefix="user_form")
        campaign_form_class = CampaignForm(prefix="campaign_form")
        context = {'user_form': user_form_class, 'campaign_form': campaign_form_class}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        user_form_class = UserForm(request.POST, prefix="user_form")
        campaign_form_class = CampaignForm(request.POST, prefix="campaign_form")
        if user_form_class.is_valid() and campaign_form_class.is_valid():
            return HttpResponseRedirect('/')
        return render(request, self.template_name, {'user_form': user_form_class, 'campaign_form': campaign_form_class})


class ContactView(CreateView):
    """
    Create contact
    """
    form_class = ContactForm
    template_name = 'core/contact_new.html'
    success_url = '/'
