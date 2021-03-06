from django.conf import settings
from django.contrib.auth import get_user_model

def get_or_none(model,**kwargs):
  try:
    return model.objects.get(**kwargs)
  except model.DoesNotExist:
    return None
  except model.MultipleObjectsReturned:
    return model.objects.filter(**kwargs)[0]

class EmailOrUsernameModelBackend(object):
  def authenticate(self, username=None, password=None):
    User = get_user_model()
    user = get_or_none(User,email__iexact=username) or get_or_none(User,username__iexact=username)
    if user and user.check_password(password):
      return user
    return None

  def get_user(self, user_id):
    User = get_user_model()
    try:
      return User.objects.get(pk=user_id)
    except User.DoesNotExist:
      return None
