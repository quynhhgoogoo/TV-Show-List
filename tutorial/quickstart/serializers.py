from django.contrib.auth.models import User, Group
from .models import Idol, Tvshow
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
class IdolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
		model = Idol
		fields = ('url', 'id', 'name')

class TvshowSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
		model = Tvshow
		fields = ('url', 'id', 'name')