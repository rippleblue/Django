from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.photo_list, name='photo_list'),
]