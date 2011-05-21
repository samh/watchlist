from watchlist.models import Show
from django.contrib import admin

class ShowAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'watch_state', 'progress')
    list_editable = ('watch_state', 'progress')
    list_filter = ('type', 'watch_state', 'production_type')
    
    #radio_fields = {"watch_state": admin.HORIZONTAL}
    
    search_fields = ['title']

admin.site.register(Show, ShowAdmin)
