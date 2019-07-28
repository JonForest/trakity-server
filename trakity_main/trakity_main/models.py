from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    description = models.TextField()
    # null=True - allow null values, blank=True - allow adding this field to be optional
    detail = models.TextField(null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    priority = models.IntegerField(null=True, blank=True)
    on_calendar = models.BooleanField(default=False)
    rollover_count = models.IntegerField(default=0)

    # Details behind auto_now_add and auto_now here https://docs.djangoproject.com/en/2.2/ref/models/fields/#datefield
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
