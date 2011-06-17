from watchlist.models import Show
from django.contrib import admin

class ShowAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'watch_state', 'progress', 'timestamp_modified')
    list_editable = ('watch_state', 'progress')
    list_filter = ('type', 'watch_state', 'production_type')
    
    date_hierarchy = 'timestamp_modified'
    
    # The submit button for the actions seems to take precedence when pressing
    # "Enter" to save the fields editable in the list.
    actions_on_top = False
    actions_on_bottom = False
    
    #radio_fields = {"watch_state": admin.HORIZONTAL}
    
    search_fields = ['title']

admin.site.register(Show, ShowAdmin)
