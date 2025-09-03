from rest_framework import serializers

from comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Comment
        fields = ['id', 'user', 'article', 'content','created_at']
        read_only_fields = ['user','created_at']
        