from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogInfo
from .forms import BlogInfoModelForm

def home(request):
    return render(request, 'blog/index.html')

def list_all_blog(request):
    data = BlogInfo.objects.all()
    context = {
        'data': data
    }
    return render(request, 'blog/list.html', context=context)

def detail_view_of_blog(request, blog_id):
    obj = BlogInfo.objects.get(blog_id=blog_id)
    return render(request, 'blog/detail.html', context={
        'obj':obj
    })

def create_blog_info(request):
    if request.method == 'POST':
        form = BlogInfoModelForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            print("Form is valid")
            form.save()
            return redirect('/blog/list/')
        else:
            print("Form is invalid")
    else:
        form = BlogInfoModelForm()
    return render(request, 'blog/create.html', {
        'form': form
    })

def update_blog_info(request, blog_id):
    obj = get_object_or_404(BlogInfo, blog_id=blog_id)
    if request.method == 'POST':
        form = BlogInfoModelForm(request.POST, instance=obj)
        if form.is_valid():
            print(form.cleaned_data)
            print("Form is valid")
            form.save()
            return redirect('/blog/list/')
        else:
            print("Form is invalid")
    else:
        form = BlogInfoModelForm(instance=obj)
    return render(request, 'blog/update.html', {
        'form': form
    })

def delete_blog_info(request, blog_id):
    # if request.method == 'POST':
    blog_object = get_object_or_404(BlogInfo, blog_id=blog_id)
    blog_object.delete()
    return redirect('/blog/list/')