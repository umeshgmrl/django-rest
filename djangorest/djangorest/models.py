from django.contrib.auth.models import User
from django.db import models

class centermaster(models.Model):
  name = models.CharField(max_length=30, unique=True)
  def __str__(self):
    return self.name

class shiftcutoff(models.Model):
  dayofweek = models.PositiveIntegerField
  cutoffhours = models.PositiveIntegerField

class shiftmaster(models.Model):
  time = models.DateTimeField()
  cutoffid = models.ForeignKey(shiftcutoff, related_name='shifts', on_delete=models.CASCADE)
  centerid = models.ForeignKey(centermaster, related_name='shifts', on_delete=models.CASCADE)

class scheduler(models.Model):
  message = models.TextField(max_length=4000)
  shiftid = models.ForeignKey(shiftcutoff, related_name='schedules', on_delete=models.CASCADE)
  userid = models.ForeignKey(User, related_name='schedules', on_delete=models.CASCADE)
  centerid = models.ForeignKey(centermaster, related_name='schedules', on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(null=True)
  def __str__(self):
    return self.message


