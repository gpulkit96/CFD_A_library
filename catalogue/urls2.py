
from django.conf.urls import url , include
from catalogue.models import Member
from . import views
urlpatterns = [
    url(r'^$', views.IndexViewMember.as_view(),name='index'),
    url(r'^(?P<pk>\d+)$', views.DetailViewMember.as_view(),name='detail'),
]
