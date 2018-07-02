from django.conf.urls import url

from core import views

urlpatterns = [
    url(r'^$', views.Dashboard.as_view(), name='dashboard'),
    url('contacts/create/$', views.ContactView.as_view(), name='create_contacts'),
]
