from django.contrib import admin
from home.models import Article, Category



@admin.action(description="published")
def make_published(modeladmin, request, queryset):
    queryset.update(status="p")
    
@admin.action(description="is_special")
def make_is_special(modeladmin, request, queryset):
    queryset.update(is_special=True)  



class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbnail_tag','slug', 'author', 'publish','is_special', 'status', 'category_to_str')
    list_filter = ('publish','status')
    list_per_page = 5
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-status', '-publish']
    actions = [make_published, make_is_special, ]
    


admin.site.register(Article, ArticleAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','slug', 'status', 'position')
    list_filter = ('status',)
    list_per_page = 10
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    
admin.site.register(Category, CategoryAdmin)