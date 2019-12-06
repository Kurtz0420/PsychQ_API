from django.conf.urls import url

from categories.api.views import CategoryRudView, CategoryApiView
from crashcourses.api.views import CrashCourseRudView, CrashCourseApiView

urlpatterns = [
    url(r'(?P<id>\w+)', CrashCourseRudView.as_view()),
    url(r'^$', CrashCourseApiView.as_view())


]
