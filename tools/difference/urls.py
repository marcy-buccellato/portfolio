from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.DifferenceView.as_view(), name='index'),
]