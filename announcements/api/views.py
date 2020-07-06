# generic views
import uuid

from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from rest_framework import generics, mixins, filters
from rest_framework.views import APIView

from announcements.api.serializers import AnnouncementSerializer
from announcements.models import Announcement
from posts.models import Post

from posts.api.serializers import PostSerializer


# ListApiView will list the posts #CreateModelMixin Will provide create
class AnnouncementApiView(
    generics.ListAPIView,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin):
    lookup_field = 'id'  # also default by django # url (?P<pk>\d+)   #if we change pk we have to change

    serializer_class = AnnouncementSerializer
    queryset = Announcement.objects.all()

    # posts_list = Post.objects.get_queryset().order_by('custom_ordering')
    # paginator = Paginator(posts_list, 20)

    # It will make sure that logged in user is associated with the post (Auto entry in post)
    def perform_create(self, serializer):
        post_id = str(uuid.uuid4()).replace("-", "")
        serializer.save()

    # Enables us to post on /api/posts
    def post(self, request, *args, **kwargs):
        post_id_ = self.kwargs.get('id')
        return self.create(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        id_ = self.kwargs.get('id')

        object_to_update = Announcement.objects.filter(id=id_).first()

        print("object_to_update", object_to_update)
        # try:
        #     object_to_update = Post.objects.get(pk=pk)
        # except Post.DoesNotExist:
        #     object_to_update= None
        serializer = AnnouncementSerializer(object_to_update, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(code=201, data=serializer.data, safe=False)
        return JsonResponse(code=400, data="Wrong Parameters", safe=False)

    # def update(self, request, *args, **kwargs):
    #     kwargs['partial'] = True
    #     return self.update(request, *args, **kwargs)

    def get_object(self):
        post_id = self.kwargs.get("id")
        return Announcement.objects.get(id=post_id)

    # def perform_update(self, serializer):
    #     instance = serializer.save()
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(code=201, data=serializer.data)
    #     return JsonResponse(code=400, data="Wrong Parameters")

    # def patch(self, request):
    #
    #     #object_to_update = self.get_object()
    #     pk = self.get('pk')
    #     object_to_update = Post.objects.filter(pk=pk)
    #     serializer = PostSerializer(object_to_update, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(code=201, data=serializer.data)
    #     return JsonResponse(code=400, data="Wrong Parameters")


class AnnouncementRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'  # also default by django # url (?P<pk>\d+)   #if we change pk we have to change lookup_field
    #  #data will be fetched by entring pk
    serializer_class = AnnouncementSerializer
    queryset = Announcement.objects.all()

    def get_queryset(self):
        return Announcement.objects.all()

#
# def get_object(self):
#     pk=self.kwargs.get("pk")
#     return Post.objects.get(pk=pk)
