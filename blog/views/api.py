from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models import Post
from ..serializers import PostSerializer


@api_view()
def post_api_list(request):
    post = Post.objects.get()
    serializer = PostSerializer(instance=post)
    return Response(serializer.data)


@api_view()
def post_api_detail(request, pk):
    post = get_object_or_404(Post.objects, pk=pk)
    serializer = PostSerializer(instance=post)
    return Response(serializer.data)
