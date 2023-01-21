from django.contrib import admin
from .models import Blog,Comment,Category

# Register your models here.

class BlogsAdmin(admin.ModelAdmin):
    list_display=('title','author','date_added','comment_count')
    list_display_links=('title',)
    prepopulated_fields={'slug':('title',)}
    
class CommentsAdmin(admin.ModelAdmin):
    list_display=('name','post','email','status','date_added')


admin.site.register(Blog,BlogsAdmin)
admin.site.register(Category)
admin.site.register(Comment,CommentsAdmin)