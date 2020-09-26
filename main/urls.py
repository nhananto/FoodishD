from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('tour', views.tour, name='tour'),
    path('contact', views.contact, name='contact'),
    path('404/', views.not_found, name='not_found')


]