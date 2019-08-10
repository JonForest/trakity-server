from rest_framework import permissions

from trakity_main.permissions import IsOwner
from trakity_main.serializers import TaskSerializer
from trakity_main.models import Task
from rest_framework_json_api.views import ModelViewSet


class TaskViewSet(ModelViewSet):
    """
    API endpoint that allows Tasks to be viewed or edited.
    """
    serializer_class = TaskSerializer
    pagination_class = None
    queryset = Task.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwner]

    def get_queryset(self):
        return Task.objects.all() \
            .filter(user_id=self.request.user.id)\
            .order_by('-start_date')
