"""PsychQAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import django
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include

# Routers provide an easy way of automatically determining the URL conf.
from django.views.generic import TemplateView
from rest_framework import routers
from categories.api.views import CategoryRudView
from orders.api.views import OrderRudView
from products.api.views import ProductRudView
from posts.api.views import PostRudView
from reviews.api.views import ReviewRudView
from unsplashcategories.api.views import UnsplashCategoryRudView

router = routers.DefaultRouter()

router.register(r'psychq/posts', PostRudView)
router.register(r'psychq/categories', CategoryRudView)
router.register(r'psychq/products', ProductRudView)
router.register(r'psychq/orders', OrderRudView)
router.register(r'psychq/reviews', ReviewRudView)
router.register(r'psychq/unsplashcategories', UnsplashCategoryRudView)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/psychq/posts/', include('posts.api.urls')),
    url(r'^api/psychq/categories/', include('categories.api.urls')),
    url(r'^api/psychq/products/', include('products.api.urls')),
    url(r'^api/psychq/orders/', include('orders.api.urls')),
    url(r'^api/psychq/reviews/', include('reviews.api.urls')),
    url(r'^api/psychq/unsplashcategories/', include('unsplashcategories.api.urls')),
    # path('accounts/', include('users.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),  # For Login Views
    path('accounts/', include('allauth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),  # HomePage 127.0.0.1:8000
    # url(r'api/v1/', include('social_django.urls', namespace='social')) #Google Auth

]
