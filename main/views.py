from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse

@login_required
def home(request):
  return TemplateResponse(request,"index.html",{})

redirect = lambda request,url: HttpResponseRedirect(url)
