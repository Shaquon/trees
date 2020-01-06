from django.shortcuts import render
from dropbox.models import Genre

# Create your views here.
from mptt.admin import MPTTModelAdmin


def show_genres(request):
    return render(request, "genres.html", {'genres': Genre.objects.all()})