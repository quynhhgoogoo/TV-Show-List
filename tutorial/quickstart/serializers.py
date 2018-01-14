from django.contrib.auth.models import User, Group
from .models import JustinBieber, EmmaWatson
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
class JustinBieberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
		model = JustinBieber
		fields = ('url', 'date_of_birth', 'alternative_name', 'sibblings_name', 'mother_name')

class EmmaWatsonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
		model = EmmaWatson
		fields = ('url', 'date_of_birth', 'nationality')