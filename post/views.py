from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Post, Tag, Category

from PIL import Image


def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post = get_object_or_404(Post, slug=slug)

    return render(request, 'post/detail.html', {
        'post': post,
    })

def tag_post(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    posts = tag.posts.all()
     
    return render(request, 'post/tag_post.html', {
        'posts': posts,
        'tag': tag,
    })

@login_required
def new(request):
    if request.method == "POST":
        title = request.POST.get('title', '')
        meta_title = request.POST.get('meta_title', '')
        summary = request.POST.get('summary', '')
        content = request.POST.get('content', '')
        image_file = request.FILES['image_file']

        categories = request.POST.getlist('categories', '')
        tags = request.POST.getlist('tags', '')

        post = Post(
            author=request.user,
            title=title,
            meta_title=meta_title,
            summary=summary,
            content=content,
            image=image_file,
        )

        post.save()
        post.categories.set(categories)
        post.tags.set(tags)

        return redirect('/my-post')
    else:
        categories = Category.objects.all()
        tags = Tag.objects.all()

    return render(request, 'post/new.html', {
        'categories': categories,
        'tags': tags,
    })

@login_required
def edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.title = request.POST.get('title', '')
        post.meta_title = request.POST.get('meta_title', '')
        post.summary = request.POST.get('summary', '')
        post.content = request.POST.get('content', '')

        # handle image
        if request.FILES.get('image_file'):
            image_file = request.FILES.get('image_file', '')
            post.image = image_file        

        categories = request.POST.getlist('categories', '')
        tags = request.POST.getlist('tags', '')
        post.categories.set(categories)
        post.tags.set(tags)

        post.save()

        return redirect('/my-post')
    else:

        # handle tags and categories of instance
        categories = Category.objects.all().values()
        tags = Tag.objects.all().values()

        for category in categories:
            if category in post.categories.all().values():
                category['selected'] = True,
            else:
                category['selected'] = False;

        for tag in tags:
            if tag in post.tags.all().values():
                tag['selected'] = True,
            else:
                tag['selected'] = False;


    return render(request, 'post/edit.html', {
        'categories': categories,
        'tags': tags,
        'post': post,
    })

@login_required
def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()

    return redirect('/my-post')
