from rest_framework import serializers

from dinglebox.models import Clip
from posts.models import Post


# Converts to JSON + Validation for data passed
class ClipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clip
        fields = [
            'id',
            'custom_ordering',
            'title',
            'description',
            'audio_link',
            'thumb_small',
            'thumb_large',
            'have_ad',
            'timestamp',
        ]
        read_only_fields = ['timestamp']

        # For Field Validation

        #  This part is not working properly, come back to it later
        def __init__(self):
            self.instance = None

        def validate_title(self, value):
            val_title = Clip.objects.filter(title__iexact=value)  # will throw error if the title of two posts is same
            if self.instance:
                val_title = val_title.exclude(id=self.instance.id)
            if val_title.exists():
                raise serializers.ValidationError("Title Already Exists..must be unique")
            return value

        def validate_id(self, value):
            val_title = Clip.objects.filter(id__iexact=value)  # will throw error if the title of two posts is same
            if self.instance:
                val_title = val_title.exclude(id=self.instance.id)
            if val_title.exists():
                raise serializers.ValidationError("Code Already Exists..must be unique")
            return value
