#######################################################
# Apps
# Tia Walker
# 04-04-24
#######################################################

from django.contrib import admin

from .models import Exhibit, Data, Play, Media

class ExhibitAdmin(admin.ModelAdmin):
    list_display = ['name','created','updated']
    ordering = ['-updated']
    #search_fields = ['exhibit']

class DataAdmin(admin.ModelAdmin):
    list_display = ['exhibit', 'created','updated']
    ordering = ['-updated']
    readonly_fields = ['exhibit', 'plays_seen', 'created', 'updated']
    #search_fields = ['exhibit', 'plays_seen']

class PlayAdmin(admin.ModelAdmin):
    list_display = ['name','created','updated']
    ordering = ['-updated']
    #search_fields = ['name']

class MediaAdmin(admin.ModelAdmin):
    list_display = ['name','created','updated']
    ordering = ['-updated']
    #search_fields = ['name']

# Register your models here.
admin.site.register(Exhibit, ExhibitAdmin)
admin.site.register(Data, DataAdmin)
admin.site.register(Play, PlayAdmin)
admin.site.register(Media, MediaAdmin)




