from django.conf import settings
from django.db import models
from django.db.models import IntegerField
from django.urls import reverse

from rest_framework.reverse import reverse as api_reverse


# Create your models here.

class Article(models.Model):
    id = models.CharField(max_length=100, null=False, blank=False, unique=True, primary_key=True)
    custom_ordering = models.IntegerField(default=0)
    title = models.CharField(max_length=120, unique=True, help_text="Name of the Post")
    description = models.CharField(max_length=1300, null=True, blank=True, help_text="Brief description")
    article_content = models.CharField(max_length=10000, null=False, blank=False, help_text="Content Of Article Goes Here")
    parent_course = models.CharField(max_length=100, null=False, blank=False, help_text="Course Name the article belongs to")
    source = models.CharField(max_length=200, null=False, blank=False, help_text="Source Of the Article", default="Human Behaviour")
    est_time = models.CharField(max_length=50, null=True, blank=False, help_text="Estimate Time of read", default="1 min read")
    thumbnail = models.CharField(max_length=1000, null=True, help_text="Thumbnail Slug of the image")
    full_res_image = models.CharField(max_length=1000, null=True, help_text="High Resolution Slug of the image - maybe from pixabay")
    universal_count = models.IntegerField(help_text="Count of article in Overall courses")  # Overall Count of whole posts
    course_count = models.IntegerField(help_text="Count of article in its parent course")  # count in a category
    tags = models.CharField(max_length=1000, null=True, blank=True, help_text="Significant words used in article for search")
    reads = models.IntegerField()

    downloads = models.IntegerField()
    shares = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id + ", " + self.title)

    def __init__(self, *args, **kwargs):
        super(Article, self).__init__(*args, **kwargs)

        # @property
    # def owner(self):
    #    return self.user
    #
    # # def get_absolute_url(self):
    # #     return reverse("api-postings:post-rud", kwargs={'pk': self.pk}) '/api/postings/1/'
    #
    # def get_api_url(self, request=None):
    #    return api_reverse("api-postings:post-rud", kwargs={'pk': self.pk}, request=request)
