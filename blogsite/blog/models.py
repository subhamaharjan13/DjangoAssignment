from django.db import models

class BlogInfo(models.Model):
    blog_id = models.IntegerField(primary_key=True)
    blog_title = models.CharField(max_length=100)
    blog_content = models.TextField()
    author_name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author_name