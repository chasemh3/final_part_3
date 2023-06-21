from django.urls import path 
from .views import indexPageView, kidsTable, personView

urlpatterns = [
    path('', indexPageView, name= 'home'),
    path('personview', personView,name='person'),
]
