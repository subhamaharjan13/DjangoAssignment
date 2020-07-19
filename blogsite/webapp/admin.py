from django.contrib import admin

from .models import BlogInfo, Author

admin.site.register(Author)
admin.site.register(BlogInfo)
