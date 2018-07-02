from rest_framework import viewsets
from board.models import Posting, Comment
from board.serializer import PostingSerializer, CommentSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


class PostingViewSet(viewsets.ModelViewSet):
    queryset = Posting.objects.all()
    serializer_class = PostingSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


@csrf_exempt
def posting_detail(request, pk):
    try:
        posting = Posting.objects.get(pk=pk)
    except Posting.DoesNotExist:
        return HttpResponse(status=404)

    if (request.method == 'GET'):
        serializer = PostingDetailSerializer(posting, context={'request' : request})
        return JsonResponse(serializer.data)
