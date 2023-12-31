from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager


# Create your models here.
class Post(models.Model):
    options = (
        ("draft", "Draft"),
        ("published", "Published"),
    )

    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="post_author"
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=options, default="draft")

    tags = TaggableManager()

    def get_absolute_url(self):
        return reverse("blog:post_single", args=[self.slug])

    class Meta:
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return self.title
