from rest_framework_json_api import serializers
from trakity_main.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        # resource_name shouldn't need to be set, but it does for some reason
        # https://django-rest-framework-json-api.readthedocs.io/en/stable/usage.html#setting-the-resource-name
        # todo: if ever have time, perhaps log error over this
        resource_name = 'tasks'
        model = Task
        # exclude = ('user', )
        fields = '__all__' # todo: remove once user added
        # read_only_fields = ('user', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')

    # def create(self, validated_data):
    #     #  Grab the current user off the request object (available on the context)
    #     user = None
    #     request = self.context.get("request")
    #     if request and hasattr(request, "user"):
    #         user = request.user
    #     validated_data['user'] = user
    #
    #     return super(TaskSerializer, self).create(validated_data)
