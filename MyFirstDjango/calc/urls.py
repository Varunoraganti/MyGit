from django.urls import path
# This is the change
from . import views
urlpatterns=[
 path('', views.home, name='home'),
 path('add',views.add, name='add'),
 path('dashboard/',views.dashboard, name='dashboard'),
]