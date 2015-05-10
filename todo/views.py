from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt

from .models import TaskList, Task

import json

MODELS = {
  "task": Task,
  "list": TaskList
}

def list_lists(request):
  return HttpResponse(json.dumps([t.json for t in TaskList.objects.filter(user=request.user)]))

@csrf_exempt
def new_list(request):
  return HttpResponse(json.dumps(TaskList.objects.create(user=request.user).json))

@csrf_exempt
def get_list(request,pk):
  tasklist = get_object_or_404(TaskList,pk=pk,user=request.user)
  if request.POST:
    tasklist.name = request.POST['name'].strip()
    tasklist.order = request.POST.get('order',None) or tasklist.order
    tasklist.save()
  return HttpResponse(json.dumps(tasklist.json))

@csrf_exempt
def delete(request,model_name,pk):
  model = MODELS[model_name]
  t = get_object_or_404(model,pk=pk,user=request.user).delete()
  return HttpResponse('')

def list_tasks(request,pk=None):
  return HttpResponse(json.dumps([t.json for t in Task.objects.filter(user=request.user,tasklist_id=pk)]))

@csrf_exempt
def new_task(request,pk):
  return HttpResponse(json.dumps(Task.objects.create(user=request.user,tasklist_id=pk).json))

@csrf_exempt
def get_task(request,pk):
  task = get_object_or_404(Task,pk=pk,user=request.user)
  if request.POST:
    task.description = request.POST['description'].strip()
    task.complete = json.loads(request.POST['complete'])
    task.order = request.POST['order']
    task.save()
  return HttpResponse(json.dumps(task.json))
