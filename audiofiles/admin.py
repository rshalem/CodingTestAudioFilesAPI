from django.contrib import admin
from audiofiles.models import *
# Register your models here.

admin.site.register(AudioBook)
admin.site.register(Podcast)
admin.site.register(Song)