from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "groups"


class Attribute(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "attributes"


class Item(models.Model):
    name = models.CharField(max_length=255)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, default=None,
                              blank=True, null=True)
    description = models.CharField(max_length=255, default=None, blank=True,
                                   null=True)
    sku = models.CharField(max_length=255)
    barcode = models.BigIntegerField(default=None, blank=True, null=True)
    quantity = models.BigIntegerField()
    supplier = models.CharField(max_length=255, default=None, blank=True,
                                null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "items"


class ItemAttribute(models.Model):
    attribute = models.ForeignKey(Attribute, on_delete=models.SET_NULL,
                                  default=None, blank=True, null=True)
    item = models.ForeignKey(Item, on_delete=models.SET_NULL,
                             default=None, blank=True, null=True,
                             related_name="attributes")
    value = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.attribute.name

    class Meta:
        verbose_name_plural = "item_attributes"
