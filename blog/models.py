from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify 

# Create your models here.
class BlogPost(models.Model):
    date = models.DateField(auto_now=True, auto_created=True)
    title = models.CharField(max_length=50, unique=True)
    author = models.ForeignKey(User, blank=False, on_delete=models.CASCADE, editable=False)
    blog_text = models.TextField()
    slug = models.SlugField(max_length=100, unique=True, db_index=True, editable=False, blank=False) # Indexing for faster lookup
    image = models.ImageField(upload_to='images', blank=True, default='images/blogpost.png')
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

        
        