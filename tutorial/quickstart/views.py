from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer, JustinBieberSerializer, EmmaWatsonSerializer
from .models import JustinBieber, EmmaWatson

class UserViewSet(viewsets.ModelViewSet):
    """ 
    API endpoint that allows users to be viewed or edited.
    """ 
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """ 
    API endpoint that allows groups to be viewed or edited.
    """ 
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
	
class JustinBieberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = JustinBieber.objects.all()
    serializer_class = JustinBieberSerializer
	
class EmmaWatsonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = EmmaWatson.objects.all()
    serializer_class = EmmaWatsonSerializer