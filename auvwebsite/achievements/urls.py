from django.urls import include, path
from . import views

urlpatterns = [path('', views.achievements, name = 'achievements')


]