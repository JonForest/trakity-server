from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    description = models.TextField
    # null=True - allow null values, blank=True - allow adding this field to be optional
    detail = models.TextField(null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    priority = models.IntegerField(null=True, blank=True)
    on_calendar = models.Boolean(default=False)
    rollover_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(blank=True)
    updated_at = models.DateTimeField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
