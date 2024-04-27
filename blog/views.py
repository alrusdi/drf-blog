from django.db.models import Count, Prefetch, Q, F
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination

from . import models, serializers


class PostListView(ListAPIView):
    http_method_names = ["options", "get"]
    serializer_class = serializers.PostSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        qs = models.Post.objects.filter(
            status=models.PostStatus.PUBLISHED,
        ).annotate(
            comments_count=Count(
                "comments",
                filter=Q(comments__status=models.CommentStatus.APPROOVED),
            ),
        ).order_by("-created_at")
        return qs


class PostDetailView(RetrieveAPIView):
    http_method_names = ["options", "get"]
    queryset = models.Post.objects.filter(
        status=models.PostStatus.PUBLISHED,
    )
    serializer_class = serializers.PostDetailSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        published_comments_qs= models.Comment.objects.filter(
            status=models.CommentStatus.APPROOVED,
        ).order_by("-created_at")

        return qs.prefetch_related(
            Prefetch("comments", queryset=published_comments_qs),
            "comments__author",
        )
