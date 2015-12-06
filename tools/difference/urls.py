from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.DifferenceView.as_view(), name='difference_index'),
    url(r'^detail/(?P<pk>[0-9]+)$', views.DifferenceDetailView.as_view(), name='difference_detail'),
]