from django.urls import path

from . import views

app_name = 'owt'
urlpatterns = [
    path('', views.index, name='index'),
]