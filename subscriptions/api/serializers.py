from rest_framework import serializers

from categories.models import Category
from subscriptions.models import Subscription
from products.models import Product
from posts.models import Post


# Converts to JSON + Validation for data passed
class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = [
            'id',
            'user_email',
            'order_id',
            'purchase_token',
            'sku_product',
            'package_name',
            'developer_payload',
            'original_json',
            'purchase_status',
            'purchase_time',
            'is_acknowledged',
            'is_auto_renewing',
	    'is_active',
            'purchase_signature'
        ]

        # read_only fields cannot be POST, PUT, PATCH passed
        read_only_fields = [
            'id',
            'timestamp'
        ]

        # For Field Validation

        #  This part is not working properly, come back to it later
        def __init__(self):
            self.instance = None

        def validate_order_id(self, value):
            val_title = Subscription.objects.filter(order_id__iexact=value)  # will throw error if the title of two posts
            # is same
            if self.instance:
                val_title = val_title.exclude(pk=self.instance.pk)
            if val_title.exists():
                raise serializers.ValidationError("Order_id Already Exists..must be unique")
            return value

        def validate_purchase_token(self, value):
            val_title = Subscription.objects.filter(purchase_token__iexact=value)  # will throw error if the title of two posts
            # is same
            if self.instance:
                val_title = val_title.exclude(pk=self.instance.pk)
            if val_title.exists():
                raise serializers.ValidationError("Purchase_token Already Exists..must be unique")
            return value
