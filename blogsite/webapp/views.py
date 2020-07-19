from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogInfo, Author
from .forms import BlogInfoModelForm, AuthorModelForm

def home(request):
    return render(request, 'webapp/index.html')

def list_all_blog(request):
    data = BlogInfo.objects.all()
    context = {
        'data': data
    }
    return render(request, 'webapp/list.html', context=context)

def detail_view_of_blog(request, user_id):
    obj = BlogInfo.objects.get(id=user_id)
    return render(request, 'webapp/detail.html', context={
        'obj':obj
    })

def add_author(request):
    if request.method == 'POST':
        form = AuthorModelForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            print("Form is valid")
            form.save()
            return redirect('/webapp/author/')
        else:
            print("Form is invalid")
    else:
        form = AuthorModelForm()
    return render(request, 'webapp/add_author.html', {
        'form': form
    })

def create_blog_info(request):
    if request.method == 'POST':
        form = BlogInfoModelForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            print("Form is valid")
            form.save()
            return redirect('/webapp/list/')
        else:
            print("Form is invalid")
    else:
        form = BlogInfoModelForm()
    return render(request, 'webapp/create.html', {
        'form': form
    })

def update_blog_info(request, user_id):
    obj = get_object_or_404(BlogInfo, id=user_id)
    if request.method == 'POST':
        form = BlogInfoModelForm(request.POST, instance=obj)
        if form.is_valid():
            print(form.cleaned_data)
            print("Form is valid")
            form.save()
            return redirect('/webapp/list/')
        else:
            print("Form is invalid")
    else:
        form = BlogInfoModelForm(instance=obj)
    return render(request, 'webapp/update.html', {
        'form': form
    })

def delete_blog_info(request, user_id):
    blog_object = get_object_or_404(BlogInfo, id=user_id)
    blog_object.delete()
    return redirect('/webapp/list/')

def list_all_author(request):
    author_data = Author.objects.all()
    context = {
        'author_data': author_data
    }
    return render(request, 'webapp/authors.html', context=context)