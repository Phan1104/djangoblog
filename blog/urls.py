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
    # =========================
    # POST LIST
    # =========================
    path(
        "",
        PostListView.as_view(),
        name="post_list",
    ),

    # =========================
    # CREATE
    # =========================
    path(
        "post/create/",
        PostCreateView.as_view(),
        name="post_create",
    ),

    # =========================
    # DETAIL
    # =========================
    path(
        "post/<slug:slug>/",
        PostDetailView.as_view(),
        name="post_detail",
    ),

    # =========================
    # UPDATE
    # =========================
    path(
        "post/<slug:slug>/edit/",
        PostUpdateView.as_view(),
        name="post_update",
    ),

    # =========================
    # DELETE
    # =========================
    path(
        "post/<slug:slug>/delete/",
        PostDeleteView.as_view(),
        name="post_delete",
    ),

    # =========================
    # OTHER PAGES
    # =========================
    path(
        "about/",
        about,
        name="about",
    ),

    path(
        "contact/",
        contact,
        name="contact",
    ),
]