from django.conf.urls import url
from django.urls import path

from dinglebox.api.views import ClipRudView, ClipApiView
from posts.api.views import PostRudView, PostApiView

urlpatterns = [
    url(r'(?P<id>\w+)', ClipRudView.as_view()),
    url(r'^$', ClipApiView.as_view())


]
