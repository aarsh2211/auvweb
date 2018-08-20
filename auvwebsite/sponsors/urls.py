from django.urls import include, path
from . import views

urlpatterns = [path('', views.sponsors, name = 'sponsors')


]