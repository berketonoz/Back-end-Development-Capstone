from django.contrib import admin

# Register your models here.
from .models import Concert, Song, Photo

admin.site.register(Concert)
admin.site.register(Photo)
admin.site.register(Song)