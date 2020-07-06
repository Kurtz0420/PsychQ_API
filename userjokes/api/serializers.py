from rest_framework import serializers

from jokes.models import Joke
from posts.models import Post


# Converts to JSON + Validation for data passed
from userjokes.models import UserJoke


class UserJokeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserJoke
        fields = [
            'id',
            'username',
            'email',
            'build_up',
            'delivery',
            'type',
            'slug',
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
