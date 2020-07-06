# generic views
import uuid

from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from rest_framework import generics, mixins, filters
from rest_framework.views import APIView

from jokes.api.serializers import JokeSerializer
from jokes.models import Joke
from posts.models import Post

from posts.api.serializers import PostSerializer


# ListApiView will list the posts #CreateModelMixin Will provide create
from userjokes.api.serializers import UserJokeSerializer
from userjokes.models import UserJoke


class UserJokeApiView(
    generics.ListAPIView,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin):
    lookup_field = 'id'  # also default by django # url (?P<pk>\d+)   #if we change pk we have to change

    # lookup_field  #data will be fetched by entring pk
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['custom_ordering', 'timestamp']  # With this we can order the posts object by the specified field by adding
    # ordering keyword e.g /api/psychq/posts/?ordering=custom_ordering&page=20

    serializer_class = UserJokeSerializer
    queryset = UserJoke.objects.all()

    # posts_list = Post.objects.get_queryset().order_by('custom_ordering')
    # paginator = Paginator(posts_list, 20)

    def get_queryset(self):
        # following will enable us to search through all posts with any parameter from model '?q={
        # value_of_field_added_below}'
        qs = UserJoke.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            if '_' in query:  # If query contains '_' it will search build_up part
                print("if Statement")
                query = query.replace(query[:1], '')
                qs = qs.filter(Q(build_up__contains=query)).distinct()

            else:
                print("Else Statement")
                qs = qs.filter(
                    Q(type__iexact=query)
                    | Q(id__iexact=query)
                    | Q(username__iexact=query)
                    | Q(email__iexact=query)

                ).distinct()  # title & cotegory for query
        return qs

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

        object_to_update = UserJoke.objects.filter(id=id_).first()

        print("object_to_update", object_to_update)
        # try:
        #     object_to_update = Post.objects.get(pk=pk)
        # except Post.DoesNotExist:
        #     object_to_update= None
        serializer = UserJokeSerializer(object_to_update, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(code=201, data=serializer.data, safe=False)
        return JsonResponse(code=400, data="Wrong Parameters", safe=False)

    # def update(self, request, *args, **kwargs):
    #     kwargs['partial'] = True
    #     return self.update(request, *args, **kwargs)

    def get_object(self):
        post_id = self.kwargs.get("id")
        return UserJoke.objects.get(id=post_id)

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


class UserJokeRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'  # also default by django # url (?P<pk>\d+)   #if we change pk we have to change lookup_field
    #  #data will be fetched by entring pk
    serializer_class = UserJokeSerializer
    queryset = UserJoke.objects.all()

    def get_queryset(self):
        return UserJoke.objects.all()

#
# def get_object(self):
#     pk=self.kwargs.get("pk")
#     return Post.objects.get(pk=pk)
