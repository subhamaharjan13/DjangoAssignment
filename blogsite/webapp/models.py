from django.db import models

class Author(models.Model):
    author_name = models.CharField(max_length=100)

class BlogInfo(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.blog_title