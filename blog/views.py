from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from .models import Post


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(
            status="published"
        ).order_by("-created_at")


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_queryset(self):
        return Post.objects.filter(
            status="published"
        )


class PostCreateView(CreateView):
    model = Post
    fields = [
        "title",
        "content",
        "category",
        "tags",
        "status"
    ]
    template_name = "blog/post_form.html"

    def get_success_url(self):
        return reverse(
            "post_detail",
            kwargs={"slug": self.object.slug}
        )


class PostUpdateView(UpdateView):
    model = Post
    fields = [
        "title",
        "content",
        "category",
        "tags",
        "status"
    ]
    template_name = "blog/post_form.html"

    def get_success_url(self):
        return reverse(
            "post_detail",
            kwargs={"slug": self.object.slug}
        )


class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    context_object_name = "post"
    success_url = reverse_lazy("post_list")

def about(request):
    return render(
        request,
        "blog/about.html",
        {"team": "DjangoBlog Team"}
    )


def contact(request):
    return render(
        request,
        "blog/contact.html"
    )