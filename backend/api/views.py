from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

# import view sets from the REST framework
from rest_framework import viewsets

# import the InternSerializer from the serializer file
from .serializers import AnalyseMatchesSerializer

# import the Intern model from the models file
from .models import AnalyseMatches

fields = [
        "id",
        "name",
        "preference1",
        "preference2",
        "preference3"
]

# create a class for the Intern model viewsets
class AnalyseMatchesView(viewsets.ModelViewSet):

    # create a serializer class and
    # assign it to the IntenSerializer class
    serializer_class = AnalyseMatchesSerializer

    # define a variable and populate it
    # with the Intern list objects
    queryset = AnalyseMatches.objects.all()

    filter_backends = [DjangoFilterBackend]
    filterset_fields = fields
    ordering_fields = fields
