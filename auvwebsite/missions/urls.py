from django.urls import include, path
from . import views

urlpatterns = [path('', views.missions, name = 'missions'),
               path('application/', views.application, name = 'application')

]