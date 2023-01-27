from rest_framework import serializers

from posts.models import Comment, Post


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = [
            'text'
        ]


class PostSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    def get_comments(self, obj):
        comments = Comment.objects.filter(post_id=obj.id)
        comments = CommentSerializer(comments, many=True).data
        return comments

    class Meta:
        model = Post
        fields = [
            'owner',
            'annotation',
            'comments'
        ]