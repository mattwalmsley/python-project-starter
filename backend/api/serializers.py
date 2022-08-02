# import serializers from the REST framework
from rest_framework import serializers

# import the todo data model
from .models import AnalyseMatches

# create a serializer class
class AnalyseMatchesSerializer(serializers.ModelSerializer):

    # create a meta class
    class Meta:
        model = AnalyseMatches
        fields = ("id", "name", "preference1", "preference2", "preference3")
