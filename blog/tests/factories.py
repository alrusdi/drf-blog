import factory
from django.contrib.auth import get_user_model

from blog.models import Comment, Post


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    email = factory.Sequence(lambda n: f"user-email-{n}@email.com")
    username = factory.Sequence(lambda n: f"user-{n}")


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    author = factory.SubFactory(UserFactory)
    title = factory.Sequence(lambda n: f"post-title-{n}")
    text = factory.Sequence(lambda n: f"post-text-{n}")
    status = "published"


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    post = factory.SubFactory(PostFactory)
    author = factory.SubFactory(UserFactory)

    text = factory.Sequence(lambda n: f"post-text-{n}")

    status = "approoved"
