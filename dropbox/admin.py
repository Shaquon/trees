from django.contrib import admin
from dropbox.models import File
from mptt.admin import DraggableMPTTAdmin

# Register your models here.
# admin.site.register(File)

admin.site.register(
    File,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title'
    ),
    list_display_links=(
        'indented_title',
    ),
)
