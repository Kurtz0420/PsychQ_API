from django.conf.urls import url

from categories.api.views import CategoryRudView, CategoryApiView
from subscriptions.api.views import SubscriptionRudView, SubscriptionApiView
from products.api.views import ProductRudView, ProductApiView

urlpatterns = [
    url(r'^(?P<id>[0-9a-f-]+)/$', SubscriptionRudView.as_view()),
    url(r'^$', SubscriptionApiView.as_view())

    # first url will take uuid as a parameter

]
