from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name='home'),
    path('404/', views.not_found, name='not_found')


]