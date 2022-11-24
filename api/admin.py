from django.contrib import admin

from .models import Group, Attribute, Item, ItemAttribute

admin.site.register(Group)
admin.site.register(Attribute)
admin.site.register(Item)
admin.site.register(ItemAttribute)
