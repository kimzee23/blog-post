from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated

from comments.models import Comment
from follows.serializers import CommentSerializer


class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
