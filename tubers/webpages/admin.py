from django.contrib import admin
from .models import TopSlider
from .models import Team
from django.utils.html import format_html

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    # to display photo to admin
    def myphoto(self, object):
        return format_html(f'<img src="{object.photo.url}" width="40"/>')

    # model admin inlines
    list_display = ('id','myphoto', 'firstName', 'role', 'create_date',)
    list_display_links = ('firstName',)
    list_editable = ('role',)
    list_filter = ('role',)
    search_fields = ('firstName', 'role',)

admin.site.register(TopSlider)
admin.site.register(Team, TeamAdmin)