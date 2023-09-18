from django.contrib import admin

from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
  list_display = ('id', 'get_username', 'get_email', 'hire_date')
  list_display_links = ('id', 'get_username')
  search_fields = ('realtor__username',)
  list_per_page = 25

  def get_username(self, obj):
        return obj.realtor.username  
  get_username.short_description = 'Username'

  def get_email(self, obj):
        return obj.realtor.email 
  get_email.short_description = 'Email'

  
admin.site.register(Realtor, RealtorAdmin)