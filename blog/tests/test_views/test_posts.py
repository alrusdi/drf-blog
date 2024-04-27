
from unittest import mock

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from blog.tests.factories import CommentFactory, PostFactory


class TestPosts(APITestCase):
    def test_show_correct_posts_list(self):
        url = reverse("blog:posts-list")

        posts = [
            PostFactory(),
            latest_post := PostFactory(),
        ]

        CommentFactory(post=latest_post)
        CommentFactory(post=latest_post)
        CommentFactory(post=latest_post, status="new")


        resp = self.client.get(url, format="json")

        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        self.assertEqual(len(resp.data["results"]), 2)

        author = latest_post.author
        self.assertEqual(
            resp.data["results"][0],
            {
                "author": {
                    "id": author.id,
                    "username": author.username,
                },
                "comments_count": 2,
                "created_at": mock.ANY,
                "id": latest_post.id,
                "status": latest_post.status,
                "text": latest_post.text,
                "title": latest_post.title,
                "updated_at": mock.ANY,
            },
        )

    def test_show_correct_post_detail(self):
        posts = [
            PostFactory(),
            PostFactory(),
        ]


        CommentFactory(post=posts[0])
        latest_comment = CommentFactory(post=posts[0])
        CommentFactory(post=posts[1])

        url = reverse("blog:post-detail", kwargs={"pk": posts[0].id})
        resp = self.client.get(url, format="json")

        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        post = posts[0]
        author = post.author
        self.assertEqual(
            resp.data,
            {
                "id": post.id,
                "title": post.title,
                "text": "post-text-0",
                "created_at": mock.ANY,
                "updated_at": mock.ANY,
                "status": "published",
                "author": {
                    "id": author.id,
                    "username": author.username,
                },
                "comments": mock.ANY,
            },
        )

        comment_author = latest_comment.author
        self.assertEqual(
            resp.data["comments"][0],
            {
                "id": latest_comment.id,
                "author": {
                    "id": comment_author.id,
                    "username": comment_author.username,
                },
                "text": latest_comment.text,
                "created_at": mock.ANY,
            },
        )
