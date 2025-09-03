from django.conf import settings
from django.db import models

from blog.models import BlogArticle
from users.models import User


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(BlogArticle, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "article")
    def __str__(self):
        return f"{self.user} likes {self.article}"