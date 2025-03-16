from django.contrib import admin
from posts.models import Comment, Follow, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "text", "pub_date", "author")
    search_fields = ("text",)
    list_filter = ("pub_date",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "text", "created", "author", "post")
    search_fields = ("text",)
    list_filter = ("created",)


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ("user", "following")
    search_fields = ("user__username", "following__username")
