from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Team
# Mongo
from rest_framework_mongoengine import serializers as mongoserializers

class TeamSerializer(mongoserializers.DocumentSerializer):
    class Meta:
        model = Team
        fields = '__all__'
##End Mongo

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')
