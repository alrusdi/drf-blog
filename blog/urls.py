from django.urls import path

from . import views

urlpatterns = [
    path("posts", views.PostListView.as_view(), name="posts-list"),
    path("post/<int:pk>", views.PostDetailView.as_view(), name="post-detail"),
]
