from django.conf.urls import patterns, include, url

urlpatterns = patterns(
  'todo.views',
  url('^$','find_all'),
  url('^(\d+)/$','find_one'),
  url('^delete/(\d+)/$','delete'),
)
