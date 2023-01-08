from django.contrib import admin
from .models import Article, Link


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'header', 'type')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Link)
