from rest_framework import viewsets

from .serializers import GroupSerializer, AttributeSerializer, ItemSerializer
from .models import Group, Attribute, Item


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('-created')
    serializer_class = GroupSerializer


class AttributeViewSet(viewsets.ModelViewSet):
    queryset = Attribute.objects.all().order_by('-created')
    serializer_class = AttributeSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by('-created')
    serializer_class = ItemSerializer
