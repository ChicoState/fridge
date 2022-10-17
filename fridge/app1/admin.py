from django.contrib import admin

from app1.models import Item, Profile

admin.site.site_header = "Food Expiry Tracker"
admin.site.site_title = "Food Expiry Tracker"
# Register your models here.


admin.site.register(Item)
admin.site.register(Profile)

