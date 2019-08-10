from rest_framework.exceptions import ValidationError
from rest_framework_json_api import serializers
from trakity_main.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        # resource_name shouldn't need to be set, but it does for some reason
        # https://django-rest-framework-json-api.readthedocs.io/en/stable/usage.html#setting-the-resource-name
        # todo: if ever have time, perhaps log error over this
        resource_name = 'tasks'
        model = Task
        exclude = ('user_id', )
        read_only_fields = ('user_id', 'created_at', 'updated_at')

    def create(self, validated_data):
        #  Grab the current user off the request object (available on the context)
        request = self.context.get("request")
        try:
            user_id = request.user.id
        except AttributeError:
            # todo: fix incorrect signature
            raise ValidationError('Missing user id', code=400)
        validated_data['user_id'] = user_id

        return super(TaskSerializer, self).create(validated_data)

# For now, don't implement `update` function. Only users who own the record should be able to update it, so there is no
# need to add the user guid to the record
