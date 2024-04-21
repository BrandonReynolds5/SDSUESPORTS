from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('home/', views.index, name='home'),  # Empty path for the root of the site

]

