from django.db import models
from portfolio.models import TechTag
from markdownx.models import MarkdownxField


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    body = MarkdownxField()
    tags = models.ManyToManyField(TechTag, blank=True)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]
