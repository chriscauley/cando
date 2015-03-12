from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Task

import json

def find_all(request):
  return HttpResponse(json.dumps([t.json for t in Task.objects.filter(user=request.user)]))

@csrf_exempt
def find_one(request,pk):
  t = get_object_or_404(Task,pk=pk,user=request.user)
  if request.POST:
    t.description = request.POST['description']
    t.complete = json.loads(request.POST['complete'])
    t.save()
  return HttpResponse(json.dumps(t.json))

@csrf_exempt
def delete(request,pk):
  t = get_object_or_404(Task,pk=pk,user=request.user).delete()
  return HttpResponse('')

@csrf_exempt
def new(request):
  return HttpResponse(json.dumps(Task.objects.create(user=request.user,description="New Task").json))
