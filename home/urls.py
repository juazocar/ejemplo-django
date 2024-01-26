from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('crear-usuario', views.crear, name='crear-usuario'),

   ]