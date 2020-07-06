from django.conf.urls import url
from django.urls import path

from announcements.api.views import AnnouncementRudView, AnnouncementApiView
from posts.api.views import PostRudView, PostApiView

urlpatterns = [
    url(r'(?P<id>\w+)', AnnouncementRudView.as_view()),
    url(r'^$', AnnouncementApiView.as_view())


]
