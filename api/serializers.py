from rest_framework import serializers

from .models import Group, Attribute, Item


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['name', 'created', 'updated']


class AttributeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Attribute
        fields = ['name']


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'group', 'attributes', 'description', 'sku',
                  'barcode', 'quantity', 'supplier', 'created', 'updated']


# class ItemAttributeSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = ItemAttribute
#         fields = ['']
