# generic views
import uuid

from django.db.models import Q
from django.http import JsonResponse
from rest_framework import generics, mixins
from rest_framework.views import APIView

from categories.api.serializers import CategorySerializer
from categories.models import Category
from crashcourses.api.serializers import CrashCourseSerializer
from crashcourses.models import CrashCourse
from posts.models import Post

from posts.api.serializers import PostSerializer


# ListApiView will list the posts #CreateModelMixin Will provide create
class CrashCourseApiView(
    generics.ListAPIView,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin):
    lookup_field = 'id'  # also default by django # url (?P<pk>\d+)   #if we change pk we have to change lookup_field  #data will be fetched by entring pk
    serializer_class = CrashCourseSerializer
    queryset = CrashCourse.objects.all()

    def get_queryset(self):
        # following will enable us to search through all posts with any parameter from model '?q={
        # value_of_field_added_below}'
        qs = CrashCourse.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(

                Q(id__icontains=query) | Q(title__icontains=query)
            ).distinct()  # title & cotegory for query
        return qs

    # It will make sure that logged in user is associated with the post (Auto entry in post)
    def perform_create(self, serializer):
        # code_ = str(uuid.uuid4()).replace("-", "")
        serializer.save()

    # Enables us to post on /api/posts
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        pk = self.kwargs.get('id')

        print("Fetched pk", pk)

        object_to_update = CrashCourse.objects.filter(id=pk).first()

        print("object_to_update", object_to_update)
        # try:
        #     object_to_update = Post.objects.get(pk=pk)
        # except Post.DoesNotExist:
        #     object_to_update= None
        serializer = CrashCourseSerializer(object_to_update, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(code=201, data=serializer.data, safe=False)
        return JsonResponse(code=400, data="Wrong Parameters", safe=False)

    # def update(self, request, *args, **kwargs):
    #     kwargs['partial'] = True
    #     return self.update(request, *args, **kwargs)

    def get_object(self):
        id_ = self.kwargs.get("id")
        return CrashCourse.objects.get(id=id_)

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


class CrashCourseRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'  # also default by django # url (?P<pk>\d+)   #if we change pk we have to change lookup_field
    #  #data will be fetched by entring pk
    serializer_class = CrashCourseSerializer
    queryset = CrashCourse.objects.all()

    def get_queryset(self):
        return CrashCourse.objects.all()

    #
    # def get_object(self):
    #     pk=self.kwargs.get("pk")
    #     return Post.objects.get(pk=pk)
