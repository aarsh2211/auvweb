from django.urls import path
from . import views

urlpatterns = [path('', views.departments, name='departments'),
               path('mechanical/', views.mechanical, name='mechanical'),
               path('software/', views.software, name='software'),
               path('embedded/', views.embedded, name='embedded')
]