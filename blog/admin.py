from django.contrib import admin
from .models import Post, Comment

# Register your models here.

# class CommentInline(admin.TabularInline): 
#     model = Comment
#     extra = 0


# class ArticleAdmin(admin.ModelAdmin): 
#     inlines = [
#         CommentInline,
        # ]


admin.site.register(Post)

# admin.site.register(Comment)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'comment', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'comment')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)