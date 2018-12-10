from django.contrib import admin
from microlly_blog.models  import *

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'edit_date',)
    search_fields = ('title',)
    list_filter = ('release_date', 'edit_date',)
admin.site.register(Post, PostAdmin)