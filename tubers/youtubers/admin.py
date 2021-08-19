from django.contrib import admin
from .models import Youtuber

# Register your models here.
class YoutuberAdmin(admin.ModelAdmin):
    def subsCount(self, object):
        return f'{object.subs_count}M'

    list_display =('id', 'name', 'subsCount', 'is_featured',)
    search_fields =('name', 'camera_type',)
    list_filter =('city', 'category',)
    list_display_links =('id', 'name',)

admin.site.register(Youtuber, YoutuberAdmin)