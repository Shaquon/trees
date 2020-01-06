from django.urls import path
from mptt.admin import DraggableMPTTAdmin

from dropbox.views import show_genres
from 
urlpatterns = [
    path('genres/', show_genres),
]