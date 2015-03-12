from django.conf.urls import patterns, include, url

urlpatterns = patterns(
  'todo.views',

  url('^list/$','list_lists'),
  url('^list/(\d+)/$','get_list'),
  url('^list/new/$','new_list'),
  url('^(list|task)/delete/(\d+)/$','delete'),

  url('^list/(\d+)/tasks/$','list_tasks'),
  url('^task/(\d+)/$','get_task'),
  url('^list/(\d+)/new/$','new_task'),
)
