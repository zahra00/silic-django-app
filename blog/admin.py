from django.contrib import admin
from .models import Article, Category


class CategoryeAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'slug', 'status')
    list_filter = ('status',)
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryeAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'category_to_str')
    list_filter = ('publish', 'status')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['status', 'publish']

    def category_to_str(self, obj):
        return "، ".join([category.title for category in obj.category.all()])
    category_to_str.short_description = "دسته‌بندی"


admin.site.register(Article, ArticleAdmin)
