from rest_framework import viewsets
from board.models import Posting, Comment
from board.serializer import PostingSerializer, CommentSerializer


class PostingViewSet(viewsets.ModelViewSet):
    queryset = Posting.objects.all()
    serializer_class = PostingSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
