from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'get_listing', 'email', 'contact_date')
  list_display_links = ('id', 'name')
  search_fields = ('name', 'email', 'listing__title')
  list_per_page = 25

  def get_listing(self, obj):
        return obj.listing.title  
  get_listing.short_description = 'Listing'

admin.site.register(Contact, ContactAdmin)