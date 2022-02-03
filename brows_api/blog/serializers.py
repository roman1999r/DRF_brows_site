from rest_framework import serializers
from rest_framework.relations import HyperlinkedIdentityField

from .models import WorkPhoto, Post, Event


class WorkPhotosListSerializer(serializers.ModelSerializer):
    """Список робочих фоток"""
    category = serializers.SlugRelatedField(slug_field="title", read_only=True)


    class Meta:
        model = WorkPhoto
        exclude = ('slug',)
        #fields = ("title", "content", "photo", "category")



class PostsListSerializer(serializers.ModelSerializer):
    """Список постів"""

    category = serializers.SlugRelatedField(slug_field="title", read_only=True)

    class Meta:
        model = Post
        exclude = ('slug',)
        #fields = ("title", "content", "photo", "category", "views", "created_at")


class PostCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = "__all__"
        #fields = ("title", "content", "photo", "category",)
        #exclude = ('slug',)


class WorkPhotoCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkPhoto
        fields = "__all__"

class EventCreateUpdateDeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = [
            'title',
            'start_date',
            'start_time',
            'name',
            'number',
            'email',
            'instagram'
        ]

