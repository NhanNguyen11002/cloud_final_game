from django.conf import settings
from django.urls import include, path
from django.contrib import admin

from welcome.views import index, health

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #path(r'^$', index),
    #path(r'^health$', health),
    #path(r'^admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('game/', include('game.urls')),
    path('gs/', include('gameserver.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
