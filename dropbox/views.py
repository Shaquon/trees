from django.shortcuts import render

from dropbox.models import File

from mptt.admin import MPTTModelAdmin


def show_genres(request):
    return render(request, "genres.html", {'genres': File.objects.all()})