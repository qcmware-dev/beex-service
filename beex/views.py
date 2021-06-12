from django.shortcuts import render
from django.contrib.auth.models import User, Group
from beex.models import User as Beex_user
from rest_framework import viewsets
from rest_framework import permissions
from beex.serializer import UserSerializer, GroupSerializer, BeexUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class BeexUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    beex_users = queryset = Beex_user.objects.all()
    serializer_class = BeexUserSerializer
    permission_classes = [permissions.IsAuthenticated]


