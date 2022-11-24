from rest_framework import serializers

from .models import Group, Attribute, Item, ItemAttribute


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name', 'created', 'updated']


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ['name']


class ItemAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemAttribute
        fields = ['attribute', 'item', 'value', 'created', 'updated']


class ItemSerializer(serializers.ModelSerializer):
    attributes = ItemAttributeSerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = ['id', 'name', 'group', 'attributes', 'description', 'sku',
                  'barcode', 'quantity', 'supplier', 'created', 'updated']
