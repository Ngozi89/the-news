from django.contrib import admin
from .models import Post, Comment, Profile
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Register post models and post admin
    """
    list_display = ('title', 'slug', 'status', 'created_on')
    """Search field."""
    search_fields = ['title', 'details']
    list_filter = ('status', 'created_on')
    summernote_fields = ('details', 'subtitle')


admin.site.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    """Search through comments."""
    search_fields = ['name', 'email', 'body']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        """Approve comment"""
        queryset.update(approved=True)
