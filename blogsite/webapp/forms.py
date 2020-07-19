from django.forms import ModelForm

from .models import BlogInfo

class BlogInfoModelForm(ModelForm):
    class Meta:
        model = BlogInfo
        fields = ['blog_title', 'blog_content']