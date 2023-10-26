from django.shortcuts import render, get_object_or_404, HttpResponse

from .models import Post, Tag


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

def new(request):

    return render(request, 'post/new.html', {
        
    })
