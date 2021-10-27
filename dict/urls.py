
from django.urls import path
from . import views

urlpatterns = [
   path('',views.dictionary, name = 'dictionary')
]