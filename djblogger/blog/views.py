from typing import List

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
