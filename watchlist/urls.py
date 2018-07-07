# Uncomment the next two lines to enable the admin:
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from rest_framework import routers

from watchlist.views import ShowViewSet

admin.autodiscover()

router = routers.DefaultRouter()
router.register('shows', ShowViewSet)

urlpatterns = [
    # Uncomment the next line to enable the admin:
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    # Redirect from root to the shows admin page
    path(r'', RedirectView.as_view(url='admin/watchlist/show/', permanent=True)),

    url(r'^api-auth/', include('rest_framework.urls')),
]
