from django.db import models
from django.conf import settings

from blog.models import BlogArticle


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")
    article = models.ForeignKey(BlogArticle, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"commented by {self.user} on {self.article}"
