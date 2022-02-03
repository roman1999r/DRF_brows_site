import datetime

from django.db.models import F
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import WorkPhoto, Post, Event
from .serializers import WorkPhotosListSerializer, PostsListSerializer, PostCreateUpdateSerializer, WorkPhotoCreateUpdateSerializer, EventCreateUpdateDeleteSerializer


class HomeStoreListView(APIView):

    def get(self, request, cnt=3):
        workphoto = WorkPhoto.objects.all()
        post = Post.objects.order_by('-views')[:cnt]
        serializerWorkPhoto = WorkPhotosListSerializer(workphoto, many=True)
        serializerPost = PostsListSerializer(post, many=True)
        return Response(
            {'WorkPhoto_List': serializerWorkPhoto.data,
             'Post_List': serializerPost.data,
            }
        )




class WorkPhotoListView(APIView):
    """Вивід списка фоток"""

    def get(self, request):
        workphoto = WorkPhoto.objects.all()
        serializer = WorkPhotosListSerializer(workphoto, many=True)
        return Response(serializer.data)


class PostListView(APIView):
    """Вивід списка постів"""

    def get(self, request):
        post = Post.objects.all()
        serializer = PostsListSerializer(post, many=True)
        return Response(serializer.data)


class PostDetailView(APIView):
    """Детальніше про пост"""

    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        post.views = F('views') + 1
        post.save()
        post.refresh_from_db()
        serializer = PostsListSerializer(post)
        return Response(serializer.data)


class PostCreateView(CreateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer

    '''
    def post(self, request):

        post = PostCreateSerializer(data=request.data)
        if post.is_valid(raise_exception=True):
            post.save()
        return Response(status=201)

    def post(self, request):
        post = request.data
        serializer = PostCreateSerializer(data=post)
        if post.is_valid(raise_exception=True):
            post_saved = serializer.save()
        return Response({"message": "Post with id `{}`  has been deleted.".format(post_saved.title)}, status=204)
'''



class WorkPhotoCreateView(CreateAPIView):
    queryset = WorkPhoto.objects.all()
    serializer_class = WorkPhotoCreateUpdateSerializer


class PostUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    lookup_field = 'slug'

class WorkPhotoUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = WorkPhoto.objects.all()
    serializer_class = WorkPhotoCreateUpdateSerializer
    lookup_field = 'slug'


class EventCreateView(CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventCreateUpdateDeleteSerializer


