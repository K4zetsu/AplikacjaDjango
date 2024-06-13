from django.contrib import admin
from .models import Games,lol

#testowa klasa
class GamesAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    search_fields = ('name','description')

admin.site.register(Games, GamesAdmin)
#aktualna klasa 
class lolAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    search_fields = ('name','description')

admin.site.register(lol, lolAdmin)


