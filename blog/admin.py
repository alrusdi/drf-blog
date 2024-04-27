from django.contrib import admin

from . import models


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

class CommentsInline(admin.StackedInline):
    model = models.Comment
    extra = 0

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "created_at")
    inlines = (CommentsInline,)
