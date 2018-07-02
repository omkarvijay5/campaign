# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# python imports

# django imports
from django.db import models
from django.core.validators import RegexValidator


# third party imports

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")


class Contact(models.Model):
    """
    Contact model contains the details of the people to which the compaign messages can be sent
    email: email id of the contact person
    phone_number: contact number of the person
    """

    email = models.EmailField(max_length=70, unique=True)

    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)


class Campaign(models.Model):
    """
    Details of the compaign that can be created
    """
    title = models.CharField(max_length=255)
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    content = models.TextField()


class Report(models.Model):
    """
    contains the report of the campaign such as messages sent, delivery status etc
    """

    campaign = models.ForeignKey('core.Campaign')
    contact = models.ForeignKey('core.Contact')
    is_delivered = models.BooleanField(default=True)
