from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
  '',
  url(r'^admin/', include(admin.site.urls)),
  url(r'^$', 'main.views.home',name='home'),
  url(r'^todo/',include('todo.urls')),
  url(r'favicon.ico$', 'main.views.redirect',
      {'url': getattr(settings,'FAVICON','/static/favicon.png')}),
  url(r'^auth/',include('django.contrib.auth.urls')),
)

if settings.DEBUG:
  urlpatterns += patterns(
    '',
    url(r'^media/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
  )