from django.conf.urls import patterns, include, url
from rest_framework import routers
from watchlist import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic import RedirectView, TemplateView

admin.autodiscover()

router = routers.DefaultRouter()
router.register('shows', views.ShowViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'watchlist_dj.views.home', name='home'),
    # url(r'^watchlist_dj/', include('watchlist_dj.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # url(r'^$', RedirectView.as_view(url='admin/watchlist/show/', permanent=True)),

    url(r'^api/', include(router.urls)),
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')),

    url(r'^.*$', TemplateView.as_view(template_name='app.html')),
)
