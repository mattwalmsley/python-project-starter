from django.shortcuts import render

# Create your views here.

# import view sets from the REST framework
from rest_framework import viewsets

# import the InternSerializer from the serializer file
from .serializers import InternSerializer

# import the Intern model from the models file
from .models import Intern

# create a class for the Intern model viewsets
class InternView(viewsets.ModelViewSet):

    # create a serializer class and
    # assign it to the IntenSerializer class
    serializer_class = InternSerializer

    # define a variable and populate it
    # with the Intern list objects
    queryset = Intern.objects.all()
