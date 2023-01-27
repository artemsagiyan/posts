from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.authtoken.admin import User

from posts.models import Post, Comment
from posts.serializers import PostSerializer, CommentSerializer


class PostView(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class CommentView(generics.CreateAPIView):
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        user = User.objects.first()

        new_comment = Comment.objects.create(
            post_id=self.kwargs['pk'],
            owner_id=user.id,
            text=self.request.data.get('text')
        )
