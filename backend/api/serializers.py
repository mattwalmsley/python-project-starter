# import serializers from the REST framework
from rest_framework import serializers

# import the todo data model
from .models import Intern
from .models import Buddy

# create a serializer class
class InternSerializer(serializers.ModelSerializer):

    # create a meta class
    class Meta:
        model = Intern
        fields = (
            'id',
            'name',
            'university',
            'course',
            'LoB',
            'location',
            'interest1',
            'interest2',
            'interest3',
            'programming1',
            'programming2',
            'request_time'
        )


class BuddySerializer(serializers.ModelSerializer):

    # create a meta class
    class Meta:
        model = Buddy
        fields = (
            'id',
            'name',
            'university',
            'course',
            'LoB',
            'location',
            'interest1',
            'interest2',
            'interest3',
            'programming1',
            'programming2',
            'time_available'
        )
