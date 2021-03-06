from django.contrib.auth.models import User
from django.db import models

class JsonModel(models.Model):
  @property
  def json(self):
    return {k:getattr(self,k) for k in self.json_properties}  
  class Meta:
    abstract = True

class TaskList(JsonModel):
  name = models.CharField(max_length=256,default="New List")
  user = models.ForeignKey(User)
  order = models.IntegerField()
  json_properties = ["name","id","order","tasks"]

  __unicode__ = lambda self: "%s: %s"%(self.user,self.name)
  def save(self,*args,**kwargs):
    if not self.order:
      self.order = self.task_set.count()
    super(TaskList,self).save(*args,**kwargs)
  @property
  def tasks(self):
    return [t.json for t in self.task_set.all()]
  class Meta:
    ordering = ('order',)

class Task(JsonModel):
  description = models.CharField(max_length=256,default="New Task")
  user = models.ForeignKey(User)
  tasklist = models.ForeignKey(TaskList,null=True,blank=True)
  complete = models.BooleanField(default=False)
  json_properties = ["description","id","user_id","complete","order"]
  order = models.IntegerField()

  __unicode__ = lambda self: "%s: %s"%(self.user,self.description)
  def save(self,*args,**kwargs):
    if not self.order:
      self.order = Task.objects.filter(tasklist=self.tasklist,user=self.user).count()
    super(Task,self).save(*args,**kwargs)
  class Meta:
    ordering = ('order',)
