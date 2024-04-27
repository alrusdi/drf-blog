from django.contrib.auth import get_user_model
from rest_framework import serializers

from . import models


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "username")


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    comments_count = serializers.IntegerField()

    class Meta:
        model = models.Post
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = models.Comment
        fields = ("id", "author", "text", "created_at")

class PostDetailSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    comments = CommentSerializer(
        many=True,
        read_only=True,
    )

    def get_field_names(self, declared_fields, info):
        expanded_fields = super().get_field_names(declared_fields, info)
        expanded_fields.append("comments")
        return expanded_fields


    class Meta:
        model = models.Post
        fields = "__all__"
