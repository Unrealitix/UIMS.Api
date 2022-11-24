from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "groups"


class Attribute(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "attributes"


class Item(models.Model):
    name = models.CharField(max_length=255)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, default=None,
                              blank=True, null=True)
    attributes = models.ManyToManyField(Attribute)
    description = models.CharField(max_length=255, default=None, blank=True,
                                   null=True)
    sku = models.CharField(max_length=255)
    barcode = models.BigIntegerField(default=None, blank=True, null=True)
    quantity = models.BigIntegerField()
    supplier = models.CharField(max_length=255, default=None, blank=True,
                                null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "items"
