from rest_framework import serializers

from posts.models import Post


# Converts to JSON + Validation for data passed
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'pk',
            'user',
            'code',
            'title',
            'description',
            'category',
            'sub_category',
            'storage_link',
            'universal_count',
            'category_count',
            'sub_post_count',
            'is_printAvailible',
            'tags',
            'views',
            'downloads',

            'timestamp',
        ]
        read_only_fields = ['pk', 'user', 'timestamp']

        # For Field Validation

        #  This part is not working properly, come back to it later
        def __init__(self):
            self.instance = None

        def validate_title(self, value):
            val_title = Post.objects.filter(title__iexact=value)  # will throw error if the title of two posts is same
            if self.instance:
                val_title = val_title.exclude(pk=self.instance.pk)
            if val_title.exists():
                raise serializers.ValidationError("Title Already Exists..must be unique")
            return value
