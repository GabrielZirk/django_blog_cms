from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
    date = models.DateField(auto_now=True)
    title = models.CharField(max_length=50, unique=True)
    author = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    excerpt = models.CharField(max_length=200)
    blog_text = models.TextField()
    slug = models.SlugField(max_length=100, unique=True, db_index=True) # Indexing for faster lookup