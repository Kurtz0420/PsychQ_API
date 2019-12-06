from rest_framework import serializers

from categories.models import Category
from crashcourses.models import CrashCourse
from posts.models import Post


# Converts to JSON + Validation for data passed
class CrashCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrashCourse
        fields = [
            'id',
            'title',
            'description',
            'pic_top',
            'pic_left',
            'pic_right',
            'count_range_from',
            'count_range_to',
            'first_article_url',
            'last_article_url',
            'tags',
            'total_articles_count'
        ]
        read_only_fields = ['timestamp']

        # For Field Validation

        #  This part is not working properly, come back to it later
        def __init__(self):
            self.instance = None

        def validate_title(self, value):
            val_title = CrashCourse.objects.filter(title__iexact=value)  # will throw error if the title of two posts is
            # same
            if self.instance:
                val_title = val_title.exclude(pk=self.instance.pk)
            if val_title.exists():
                raise serializers.ValidationError("Title Already Exists..must be unique")
            return value

        def validate_id(self, value):
            val_title = CrashCourse.objects.filter(
                id__iexact=value)  # will throw error if the title of two posts is same
            if self.instance:
                val_title = val_title.exclude(pk=self.instance.pk)
            if val_title.exists():
                raise serializers.ValidationError("Title Already Exists..must be unique")
            return value
