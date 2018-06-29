from django.conf.urls import url, include
from board.models import Posting, Comment
from rest_framework import serializers


class PostingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Posting
        fields = ('url', 'name', 'title')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('url', 'posting', 'name', 'text')