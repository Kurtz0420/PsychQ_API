from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

from posts.models import Post

User = get_user_model


class PostApiTestCase(APITestCase):
    def setUp(self):
        user_obj = User()
        user_obj.set_password("raw_password")
        user_obj.save()
        post = Post.objects.create(
            user= user_obj,
            title='testTitle',
            category='testCategory',
            storage_link='testLink',
            counter_id='123sdjva'
        )

    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count,1)

    def test_single_post(self):
        post_count=Post.objects.count()
        self.assertEqual(post_count,1)
