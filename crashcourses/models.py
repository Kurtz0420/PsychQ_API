from django.conf import settings
from django.db import models
from django.db.models import IntegerField
from django.urls import reverse

from rest_framework.reverse import reverse as api_reverse


# Create your models here.

class CrashCourse(models.Model):

    id = models.CharField(max_length=100, null=False, blank=False, unique=True, primary_key=True, help_text="Unique Id")
    title = models.CharField(max_length=120, unique=True, help_text="Name of the Crash Course")
    description = models.CharField(max_length=1300, null=True, blank=True, help_text="Brief Description")

    pic_top = models.CharField(max_length=300)
    pic_left = models.CharField(max_length=300)
    pic_right = models.CharField(max_length=300)
    count_range_from = models.IntegerField(help_text="Universal Count in Articles where this CrashCourse starts")
    count_range_to = models.IntegerField(help_text="Universal Count in Articles where this CrashCourse ends")
    first_article_url = models.CharField(max_length=250, null=False, blank=False, help_text="Url of first article in Crash Course")
    last_article_url = models.CharField(max_length=250, null=False, blank=False, help_text="Url of first article in Crash Course")
    tags = models.CharField(max_length=500, help_text="Tags for modified searching")
    total_articles_count = models.IntegerField()

    def __str__(self):
        return str(self.id + ", " + self.title)

    def __init__(self, *args, **kwargs):
        super(CrashCourse, self).__init__(*args, **kwargs)

        # @property
    # def owner(self):
    #    return self.user
    #
    # # def get_absolute_url(self):
    # #     return reverse("api-postings:post-rud", kwargs={'pk': self.pk}) '/api/postings/1/'
    #
    # def get_api_url(self, request=None):
    #    return api_reverse("api-postings:post-rud", kwargs={'pk': self.pk}, request=request)
