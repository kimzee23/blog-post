from rest_framework import serializers

from blog.models import BlogArticle


class BlogArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogArticle
        fields =[
            "id",
            "title",
            "content",
            "slug",
            "hero_image",
            "hero_image_url",
            "tags",
            "author",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["slug","created_at", "updated_at"]