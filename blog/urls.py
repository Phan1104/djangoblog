from django.urls import path

from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    about,
    contact,
)


urlpatterns = [

    # Read - Post List
    path(
        "",
        PostListView.as_view(),
        name="post_list"
    ),

    # Create - Create new Post
    path(
        "posts/new/",
        PostCreateView.as_view(),
        name="post_create"
    ),

    # Update - Edit Post
    path(
        "posts/<slug:slug>/edit/",
        PostUpdateView.as_view(),
        name="post_update"
    ),

    # Delete - Delete Post
    path(
        "posts/<slug:slug>/delete/",
        PostDeleteView.as_view(),
        name="post_delete"
    ),

    # Read - Post Detail
    path(
        "posts/<slug:slug>/",
        PostDetailView.as_view(),
        name="post_detail"
    ),

    # About
    path(
        "about/",
        about,
        name="about"
    ),

    # Contact
    path(
        "contact/",
        contact,
        name="contact"
    ),

]