from rest_framework import serializers

from categories.models import Category
from orders.models import Order
from products.models import Product
from posts.models import Post


# Converts to JSON + Validation for data passed
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'order_id',
            'product_id',
            'user_id',
            'country',
            'phone_number_with_code',
            'full_address',
            'state',
            'zip_code',
            'cc_number',
            'cc_expiry',
            'cc_code',
            'order_status',
            'timestamp'
        ]

        # read_only fields cannot be POST, PUT, PATCH passed
        read_only_fields = [
            'order_id',
            'timestamp'
        ]

        # For Field Validation

        #  This part is not working properly, come back to it later
        def __init__(self):
            self.instance = None

        def validate_order_id(self, value):
            val_title = Order.objects.filter(order_id__iexact=value)  # will throw error if the title of two posts
            # is same
            if self.instance:
                val_title = val_title.exclude(pk=self.instance.pk)
            if val_title.exists():
                raise serializers.ValidationError("Order_id Already Exists..must be unique")
            return value
