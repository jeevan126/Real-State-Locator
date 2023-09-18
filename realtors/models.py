from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Realtor(models.Model):
  realtor = models.ForeignKey(User, on_delete=models.CASCADE)
  photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
  description = models.TextField(blank=True)
  phone = models.CharField(max_length=20)
  is_mvp = models.BooleanField(default=False)
  hire_date = models.DateTimeField(default=datetime.now, blank=True)

  def __str__(self):
    return self.realtor.username