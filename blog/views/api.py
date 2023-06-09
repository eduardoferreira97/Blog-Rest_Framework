from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models import Post
from ..serializers import PostSerializer


@api_view(http_method_names=['get', 'post'])
def post_api_list(request):
    if request.method == 'GET':
        post = Post.objects.filter()
        serializer = PostSerializer(
            instance=post, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data,
                        status=status.HTTP_201_CREATED)


@api_view(['get', 'patch', 'delete'])
def post_api_detail(request, pk):

    post = get_object_or_404(Post.objects, pk=pk)

    if request.method == 'GET':

        serializer = PostSerializer(
            instance=post,
            context={'request': request},
            many=True)

        return Response(serializer.data)

    elif request.method == 'PATCH':

        serializer = PostSerializer(
            instance=post,
            data=request.data,
            context={'request': request},
            partial=True,
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
