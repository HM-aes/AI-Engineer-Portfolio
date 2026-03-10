from django.views.generic import ListView, DetailView
from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import BlogPost
import markdown


class BlogListView(ListView):
    template_name = "blog/blog_list.html"
    model = BlogPost
    context_object_name = "posts"

    def get_queryset(self):
        return BlogPost.objects.filter(published=True)


class BlogDetailView(DetailView):
    template_name = "blog/blog_detail.html"
    model = BlogPost
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Markdown rendering handled via template or here.
        # Using markdown library to convert body safe string
        context["rendered_body"] = markdown.markdown(
            self.object.body, extensions=["fenced_code", "codehilite"]
        )
        return context


class LatestEntriesFeed(Feed):
    title = "Hassan Mohamed — Engineering Log"
    link = "/blog/"
    description = (
        "Updates on RAG architecture, secure AI deployments, and engineering thoughts."
    )

    def items(self):
        return BlogPost.objects.filter(published=True).order_by("-created_at")[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        # Provide a short truncate for the feed
        return markdown.markdown(item.body)[:200] + "..."

    def item_link(self, item):
        return reverse("blog-detail", args=[item.slug])
