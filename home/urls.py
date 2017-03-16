from django.conf.urls import url
from . import views

urlpatterns = [
	#url(r'^$', views.View.as_view(),name='view'),
    url(r'^$', views.index, name='index'),
    url(r'bing', views.bing, name='index'),
    url(r'trending', views.trending, name='index'),
]