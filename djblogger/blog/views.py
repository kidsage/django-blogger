from django.views.generic import ListView

from .models import Post


class HomeView(ListView):
    model = Post
    context_object_name = "posts"
    paginate_by = 5

    def get_template_names(self):
        if self.request.htmx:
            print("get test")
            # return "blog/components/post-list-elements.html"
        return "blog/index.html"
