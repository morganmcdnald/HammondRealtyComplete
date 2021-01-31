from django.contrib import admin
from .models import Neighbourhood

# Register your models here.
class NeighbourhoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(Neighbourhood, NeighbourhoodAdmin)