from rest_framework import serializers

from categories.models import Category
from products.models import Product
from posts.models import Post


# Converts to JSON + Validation for data passed
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'quantity_in_stock',
            'sales',
            'price',
            'shipment_charges',
            'photos'
        ]
        read_only_fields = []

        # For Field Validation

        #  This part is not working properly, come back to it later
        def __init__(self):
            self.instance = None

        def validate_id(self, value):
            val_title = Product.objects.filter(id__iexact=value)  # will throw error if the title of two posts is same
            if self.instance:
                val_title = val_title.exclude(pk=self.instance.pk)
            if val_title.exists():
                raise serializers.ValidationError("Title Already Exists..must be unique")
            return value
