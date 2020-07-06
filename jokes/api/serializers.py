from rest_framework import serializers

from jokes.models import Joke
from posts.models import Post


# Converts to JSON + Validation for data passed
class JokeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Joke
        fields = [
            'id',
            'custom_ordering',
            'about',
            'build_up',
            'delivery',
            'type',
            'thumb_slug',
            'full_slug',
            'gif_slug',
            'nsfw',
            'religious',
            'political',
            'thumbs_ups',
            'thumbs_downs',
            'timestamp',
        ]
        read_only_fields = ['timestamp']

        # For Field Validation

        #  This part is not working properly, come back to it later
        def __init__(self):
            self.instance = None

        def validate_build_up(self, value):
            val_title = Joke.objects.filter(build_up__iexact=value)  # will throw error if the title of two posts is same
            if self.instance:
                val_title = val_title.exclude(id=self.instance.id)
            if val_title.exists():
                raise serializers.ValidationError("Joke Already Been Told Here..Try Something Else")
            return value

        def validate_id(self, value):
            val_title = Joke.objects.filter(id__iexact=value)  # will throw error if the title of two posts is same
            if self.instance:
                val_title = val_title.exclude(id=self.instance.id)
            if val_title.exists():
                raise serializers.ValidationError("Joke Id Already Exists..must be unique")
            return value
