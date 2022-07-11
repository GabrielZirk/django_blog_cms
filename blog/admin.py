from django.contrib import admin
from blog.models import BlogPost

# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')
    ordering = ('-date',)
    
    class Meta:
        verbose_name_plural = 'Blogpost'
        

admin.site.register(BlogPost, BlogPostAdmin)