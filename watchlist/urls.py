# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView

admin.autodiscover()

urlpatterns = [
    # Uncomment the next line to enable the admin:
    path('admin/', admin.site.urls),

    # Redirect from root to the shows admin page
    path(r'', RedirectView.as_view(url='admin/watchlist/show/', permanent=True)),
]
