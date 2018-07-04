from django.conf.urls import url, include
from board.models import Posting, Comment
from rest_framework import serializers


class PostingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Posting
        fields = ('created_at', 'url', 'name', 'title')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('name', 'text')


class PostingDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Posting
        fields = ('name', 'title', 'text', 'created_at', 'updated_at')
