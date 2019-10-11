from django.conf import settings
from django.db import models
from django.db.models import IntegerField
from django.urls import reverse

from rest_framework.reverse import reverse as api_reverse


# Create your models here.

class Post(models.Model):
    id = models.CharField(max_length=100, null=False, blank=False, unique=True, primary_key=True)
    title = models.CharField(max_length=120, unique=True)
    description = models.CharField(max_length=1300, null=True, blank=True)
    category = models.CharField(max_length=120, null=True)
    sub_category = models.CharField(max_length=120, null=True, blank=True)
    storage_link = models.CharField(max_length=1000, null=True)
    universal_count = models.IntegerField()  # Overall Count of whole posts
    category_count = models.IntegerField()  # count in a category
    sub_post_count = models.IntegerField(null=True, blank=True)  # sub posts count (if any)
    is_printable = models.BooleanField(default=False)
    tags = models.CharField(max_length=1000, null=True, blank=True)
    views = models.IntegerField()
    downloads = models.IntegerField()
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
