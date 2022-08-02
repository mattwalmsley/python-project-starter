from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

# import view sets from the REST framework
from rest_framework import viewsets

# import the InternSerializer from the serializer file
from .serializers import InternSerializer
from .serializers import BuddySerializer

# import the Intern model from the models file
from .models import Intern
from .models import Buddy

fields = [
        "id",
        "name",
        "university",
        "course",
        "LoB",
        "location",
        "interest1",
        "interest2",
        "interest3",
        "programming1",
        "programming2",
    ]

# create a class for the Intern model viewsets
class InternView(viewsets.ModelViewSet):

    # create a serializer class and
    # assign it to the IntenSerializer class
    serializer_class = InternSerializer

    # define a variable and populate it
    # with the Intern list objects
    queryset = Intern.objects.all()

    filter_backends = [DjangoFilterBackend]
    filterset_fields = fields
    ordering_fields = fields


class BuddyView(viewsets.ModelViewSet):

    # create a serializer class and
    # assign it to the IntenSerializer class
    serializer_class = BuddySerializer

    # define a variable and populate it
    # with the Intern list objects
    queryset = Buddy.objects.all()

    filter_backends = [DjangoFilterBackend]
    filterset_fields = fields
    ordering_fields = fields
