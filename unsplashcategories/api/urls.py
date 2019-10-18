from django.conf.urls import url

from categories.api.views import CategoryRudView, CategoryApiView
from unsplashcategories.api.views import UnsplashCategoryRudView, UnsplashCategoryApiView

urlpatterns = [
    url(r'(?P<id>\w+)', UnsplashCategoryRudView.as_view()),
    url(r'^$', UnsplashCategoryApiView.as_view())


]
