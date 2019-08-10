from typing import Any

from django.views import View
from rest_framework import permissions
from rest_framework.request import Request


class IsOwner(permissions.BasePermission):
    """
    Custom permission that allows only the owner of a task to see it
    """
    def has_object_permission(self, request: Request, view: View, obj: Any):
        return obj.user_id == request.user.id
