from django.contrib import admin
from .models import Post, PostLikes, PostComments, CommentLikes


# Register your models here.
class PostLikeAdmin(admin.TabularInline):
    model = PostLikes


class PostAdmin(admin.ModelAdmin):
    inlines = [PostLikeAdmin]
    list_display = ['__str__', 'user']
    search_fields = ['post_description', 'user_username', 'user__email']

    class Meta:
        model = Post


class CommentLikesAdmin(admin.TabularInline):
    model = CommentLikes


class CommentAdmin(admin.ModelAdmin):
    inlines = [CommentLikesAdmin]
    list_display = ['__str__', 'user']
    search_fields = ['comment']

    class Meta:
        model = PostComments


admin.site.register(Post, PostAdmin)
admin.site.register(PostComments, CommentAdmin)
