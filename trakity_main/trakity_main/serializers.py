from rest_framework_json_api import serializers
from trakity_main.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = ('user', )
        read_only_fields = ('user', 'created_at', 'updated_at')

    def create(self, validated_data):
        #  Grab the current user off the request object (available on the context)
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        validated_data['user'] = user

        return super(TaskSerializer, self).create(validated_data)
