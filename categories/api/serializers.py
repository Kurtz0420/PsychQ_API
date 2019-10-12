from rest_framework import serializers

from categories.models import Category
from posts.models import Post


# Converts to JSON + Validation for data passed
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'title',
            'description',
            'sub_categories',
            'pic_top',
            'pic_left',
            'pic_right',
            'count_range_from',
            'count_range_to',
            'tags',
            'total_posts_count'
        ]
        read_only_fields = ['timestamp']

        # For Field Validation

        #  This part is not working properly, come back to it later
        def __init__(self):
            self.instance = None

        def validate_title(self, value):
            val_title = Category.objects.filter(title__iexact=value)  # will throw error if the title of two posts is
            # same
            if self.instance:
                val_title = val_title.exclude(pk=self.instance.pk)
            if val_title.exists():
                raise serializers.ValidationError("Title Already Exists..must be unique")
            return value

        def validate_id(self, value):
            val_title = Category.objects.filter(
                id__iexact=value)  # will throw error if the title of two posts is same
            if self.instance:
                val_title = val_title.exclude(pk=self.instance.pk)
            if val_title.exists():
                raise serializers.ValidationError("Title Already Exists..must be unique")
            return value
