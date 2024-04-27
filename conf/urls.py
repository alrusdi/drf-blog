from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/blog/", include(("blog.urls", "blog"), namespace="blog")),
]
