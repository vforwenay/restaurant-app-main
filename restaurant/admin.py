from django.contrib import admin

# Register your models here.

from .models import Item, Restaurant, Menu

admin.site.register(Menu)
admin.site.register(Restaurant)
admin.site.register(Item)