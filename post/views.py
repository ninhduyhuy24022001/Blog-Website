from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Post, Tag, Category

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
        image_file = request.POST.get('image_file', '')
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

        return redirect('/myaccount')
    else:
        categories = Category.objects.all()
        tags = Tag.objects.all()

    return render(request, 'post/new.html', {
        'categories': categories,
        'tags': tags,
    })
