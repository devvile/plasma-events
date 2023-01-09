from django.contrib import admin
from .models import Article, Link, Bullet


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'header', 'type')


class BulletAdmin(admin.ModelAdmin):
    list_display = ('name', 'list', 'text')



admin.site.register(Article, ArticleAdmin)
admin.site.register(Link)
admin.site.register(Bullet, BulletAdmin)
