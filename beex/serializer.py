from django.contrib.auth.models import User, Group
from rest_framework import serializers
#my models
from beex.models import User as Beex_user

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class BeexUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Beex_user
        print("_______\n", model.objects.all(), "\n-------")
        fields = ['username', 'email', 'phone']
