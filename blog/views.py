from rest_framework import generics, permissions

from blog.models import BlogArticle
from blog.serializers import BlogArticleSerializer


class BlogArticleListCreateView(generics.ListCreateAPIView):
    queryset = BlogArticle.objects.all()
    serializer_class = BlogArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
class BlogArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogArticle.objects.all()
    serializer_class = BlogArticleSerializer
    lookup_field = 'slug'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]