# generic views
from django.db.models import Q
from rest_framework import generics, mixins
from posts.models import Post

from posts.api.serializers import PostSerializer


# ListApiView will list the posts #CreateModelMixin Will provide create
class PostApiView(generics.ListAPIView,
                  mixins.CreateModelMixin):
    lookup_field = 'pk'  # also default by django # url (?P<pk>\d+)   #if we change pk we have to change lookup_field  #data will be fetched by entring pk
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get_queryset(self):
        # following will enable us to search through all posts with any parameter from model '?q={value_of_field_added_below}'
        qs = Post.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                Q(title__icontains=query) | Q(category__icontains=query)).distinct()  # title & cotegory for query
        return qs

    # It will make sure that logged in user is associated with the post (Auto entry in post)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # Enables us to post on /api/posts
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'  # also default by django # url (?P<pk>\d+)   #if we change pk we have to change lookup_field
    #  #data will be fetched by entring pk
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get_queryset(self):
        return Post.objects.all()

    #
    # def get_object(self):
    #     pk=self.kwargs.get("pk")
    #     return Post.objects.get(pk=pk)
