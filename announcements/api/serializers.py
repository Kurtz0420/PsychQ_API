from rest_framework import serializers

from announcements.models import Announcement
from posts.models import Post


# Converts to JSON + Validation for data passed
class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = [
            'id',
            'heading',
            'message'
        ]
