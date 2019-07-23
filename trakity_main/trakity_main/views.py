from trakity_main.serializers import TaskSerializer
from trakity_main.models import Task
from rest_framework_json_api.views import ModelViewSet


class TaskViewSet(ModelViewSet):
    """
    API endpoint that allows Tasks to be viewed or edited.
    """
    serializer_class = TaskSerializer
    pagination_class = None

    def get_queryset(self):
        return Task.objects.all()\
            .order_by('-start_date')
    # .filter(user=self.request.user)\
