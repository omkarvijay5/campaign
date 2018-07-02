from django.conf.urls import url

from core import views

urlpatterns = [
    url('', views.Dashboard.as_view(), name='dashboard'),
]
