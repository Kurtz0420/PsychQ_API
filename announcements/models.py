from django.conf import settings
from django.db import models
from django.db.models import IntegerField
from django.urls import reverse

from rest_framework.reverse import reverse as api_reverse


# Create your models here.

class Announcement(models.Model):
    id = models.CharField(max_length=100, null=False, blank=False, unique=True, primary_key=True, help_text="Accepted Input : FeedsAnnouncement, CategoryAnnouncement, CrashCourseAnnouncement")
    heading = models.CharField(max_length=120, help_text="Heading Of The Announcement")
    message = models.CharField(max_length=1300, null=True, blank=True, help_text="Message Of The Announcement")

