from django.conf import settings
from django.db import models
from django.db.models import IntegerField
from django.urls import reverse

from rest_framework.reverse import reverse as api_reverse


# Create your models here.

class Post(models.Model):
    id = models.CharField(max_length=100, null=False, blank=False, unique=True, primary_key=True)
    title = models.CharField(max_length=120, unique=True, help_text="Name of the Post")
    description = models.CharField(max_length=1300, null=True, blank=True, help_text="Brief description")
    category = models.CharField(max_length=120, null=True, help_text="Category, the Post belongs to")
    sub_category = models.CharField(max_length=120, null=True, blank=True, help_text="If the Post is from a sub category")
    thumbnail = models.CharField(max_length=1000, null=True, help_text="Thumbnail Slug of the image")
    full_res_image = models.CharField(max_length=1000, null=True, help_text="Slug of the image")
    universal_count = models.IntegerField(help_text="Count of post in Overall posts")  # Overall Count of whole posts
    category_count = models.IntegerField(help_text="Count of Post in a category")  # count in a category
    sub_post_count = models.IntegerField(null=True, blank=True, help_text="Count of post in sub category (if any)")  # sub posts count (if any)
    is_printable = models.BooleanField(default=False, help_text="Can it be printed on t-Shirt")
    tags = models.CharField(max_length=1000, null=True, blank=True, help_text="Significant words used in Post")
    views = models.IntegerField()
    downloads = models.IntegerField()
    custom_ordering = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id + ", " + self.title)

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)

        # @property
    # def owner(self):
    #    return self.user
    #
    # # def get_absolute_url(self):
    # #     return reverse("api-postings:post-rud", kwargs={'pk': self.pk}) '/api/postings/1/'
    #
    # def get_api_url(self, request=None):
    #    return api_reverse("api-postings:post-rud", kwargs={'pk': self.pk}, request=request)
