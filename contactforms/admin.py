from django.contrib import admin
from .models import Contactform

# Register your models here.
class ContactformAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'subject', 'email', 'contact_date')
    list_display_links = ('id', 'name', 'subject')
    search_fields = ('name', 'email', 'listing')
    list_per_page = 25

admin.site.register(Contactform, ContactformAdmin)