from django.forms import ModelForm

from .models import BlogInfo, Author

class BlogInfoModelForm(ModelForm):
    class Meta:
        model = BlogInfo
        fields = ['author', 'blog_title', 'blog_content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].queryset = Author.objects.all()

class AuthorModelForm(ModelForm):
    class Meta:
        model = Author
        fields = ['author_name']