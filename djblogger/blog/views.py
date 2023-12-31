from typing import List

from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView

from .models import Post


class HomeView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "blog/index.html"
    paginate_by = 5

    def get_template_names(self) -> List[str]:
        if self.request.htmx:
            return ["blog/components/post-list-elements.html"]
        return [self.template_name]


def post_single(request, post):
    post = get_object_or_404(Post, slug=post, status="published")
    related = Post.objects.filter(author=post.author)[:5]
    return render(
        request,
        "blog/single.html",
        {
            "post": post,
            "related": related,
        },
    )
