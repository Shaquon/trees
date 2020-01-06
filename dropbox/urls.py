from django.urls import path
from mptt.admin import DraggableMPTTAdmin

from dropbox.views import tree_view, login_view, register_user_view,logout_view, new_file_view

urlpatterns = [
    path('login/', login_view, name="loginview"),
    path('register/', register_user_view, name="registerview"),
    path('home/', tree_view, name="home"),
    path('newfile', new_file_view, name='newfile'),
    path('logout/', logout_view, name='logout')
]