from django.urls import path
from . import views


app_name = 'battles'

urlpatterns = [
    path('', views.index, name='index'),
]
