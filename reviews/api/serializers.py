from rest_framework import serializers

from categories.models import Category
from orders.models import Order
from products.models import Product
from posts.models import Post


# Converts to JSON + Validation for data passed
from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    # id = serializers.SlugRelatedField(
    #     read_only=True,
    #     slug_field='uuid',
    #     # queryset=Review.objects.all()  # Might be redundant with read_only=True
    # )

    class Meta:
        model = Review
        fields = [
            'id',
            'product_id',
            'user_id',
            'title',
            'description',
            'timestamp'
        ]
        read_only_fields = ['id', 'timestamp']

        # For Field Validation

        #  This part is not working properly, come back to it later
        def __init__(self):
            self.instance = None
