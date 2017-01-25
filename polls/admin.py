from django.contrib import admin
from polls.models import Item
# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    search_fields = ('article_description', 'article_id', )


admin.site.register(Item, ItemAdmin)
