from django.db import models


class Post(models.Model):
    StatusChoices = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]   
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)
    published_date = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    reading_minute = models.PositiveIntegerField()
    content_markdown = models.TextField()
    content_html = models.TextField()
    tg_link = models.URLField()
    is_published = models.BooleanField(default=False)
    status = models.CharField(choices=StatusChoices, default='draft')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
