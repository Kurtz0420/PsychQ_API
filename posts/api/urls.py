from django.conf.urls import url
from django.urls import path

from posts.api.views import PostRudView, PostApiView

urlpatterns = [
    url(r'(?P<id>\w+)', PostRudView.as_view()),
    url(r'^$', PostApiView.as_view())


]
