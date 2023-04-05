from django.contrib import admin
from .models import Post,Author,Tag,Comment,Staff,Category, About, SiteUsers

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display=("title",)
    list_filter=("author","date","tags",)

class CommentAdmin(admin.ModelAdmin):
    list_filter=("post","name")

admin.site.register(Post,PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Staff)
admin.site.register(About)
admin.site.register(SiteUsers)