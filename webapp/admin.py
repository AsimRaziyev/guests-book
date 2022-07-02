from django.contrib import admin

# Register your models here.
from webapp.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'authorName', 'authorEmail', 'created_at']
    list_display_links = ['authorName']
    list_filter = ['authorName', 'authorEmail']
    search_fields = ['authorName', 'authorEmail', 'content']
    fields = ['authorName', 'authorEmail', 'content', 'status', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Article, ArticleAdmin)
