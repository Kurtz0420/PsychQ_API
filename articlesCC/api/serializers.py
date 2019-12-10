from rest_framework import serializers

from articlesCC.models import Article
from posts.models import Post


# Converts to JSON + Validation for data passed
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'id',
            'custom_ordering',
            'title',
            'description',
            'article_content',
            'parent_course',
            'source',
            'est_time',
            'thumbnail',
            'full_res_image',
            'universal_count',
            'course_count',
            'tags',
            'reads',
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
            val_title = Article.objects.filter(title__iexact=value)  # will throw error if the title of two posts is same
            if self.instance:
                val_title = val_title.exclude(id=self.instance.id)
            if val_title.exists():
                raise serializers.ValidationError("Title Already Exists..must be unique")
            return value

        def validate_id(self, value):
            val_title = Article.objects.filter(id__iexact=value)  # will throw error if the title of two posts is same
            if self.instance:
                val_title = val_title.exclude(id=self.instance.id)
            if val_title.exists():
                raise serializers.ValidationError("Code Already Exists..must be unique")
            return value
