from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse

@login_required
def home(request):
  return TemplateResponse(request,"index.html",{'title': 'CanDo'})

redirect = lambda request,url: HttpResponseRedirect(url)

@login_required
def riot(request):
  return TemplateResponse(request,"riot.html",{'title': 'ToDo: Riot!'})
