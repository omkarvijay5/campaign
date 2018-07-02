# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# python imports

# django imports
from django.shortcuts import render
from django.views.generic import View

# third party imports


class Dashboard(View):
    """
    Dashboard is the main dashboard of the campaign
    Dashboard has multiple forms which enables to create a campaign
    """
    template_name = 'core/dashboard.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})
