from rest_framework import serializers

from posts.models import Post


# Converts to JSON + Validation for data passed
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'custom_ordering',
            'title',
            'description',
            'category',
            'sub_category',
            'thumbnail',
            'full_res_image',
            'is_trial_content',
            'universal_count',
            'category_count',
            'sub_post_count',
            'is_printable',
            'tags',
            'views',
            'downloads',
            'shares',
            'timestamp',
        ]
        read_only_fields = ['timestamp']

        # For Field Validation

        #  This part is not working properly, come back to it later
        def __init__(self):
            self.instance = None

        def validate_title(self, value):
            val_title = Post.objects.filter(title__iexact=value)  # will throw error if the title of two posts is same
            if self.instance:
                val_title = val_title.exclude(id=self.instance.id)
            if val_title.exists():
                raise serializers.ValidationError("Title Already Exists..must be unique")
            return value

        def validate_id(self, value):
            val_title = Post.objects.filter(id__iexact=value)  # will throw error if the title of two posts is same
            if self.instance:
                val_title = val_title.exclude(id=self.instance.id)
            if val_title.exists():
                raise serializers.ValidationError("Code Already Exists..must be unique")
            return value
