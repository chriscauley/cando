from django.contrib.auth.models import User
from django.db import models

class Task(models.Model):
  description = models.CharField(max_length=256)
  user = models.ForeignKey(User)
  json_properties = ["description","id","user_id"]
  @property
  def as_json(self):
    return {k:getattr(self,k) for k in self.json_properties}
  __unicode__ = lambda self: "%s: %s"%(self.user,self.description)
