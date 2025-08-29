from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class BlogArticle(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="articles"
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    hero_image_url = models.URLField(blank=True, null=True)
    hero_image = models.ImageField(blank=True, null=True, upload_to="blogs/")
    tags = models.JSONField(default=list, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super().save(*args, **kwargs)

    def __str__(self):
        return self.title