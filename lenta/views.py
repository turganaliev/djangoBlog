from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from lenta.models import Post, Comment

# Create your views here.

@csrf_exempt
def add_post(request):
    if request.method == 'POST':
        data = request.POST
        post = Post.objects.create(
            title = data['title'], image = data['image'], description = data['description']
        )
        return HttpResponse('Post created')
    if request.method == 'GET':
        return render(request, 'add-post.html')
    else:
        return HttpResponse('Method not allowed')

@csrf_exempt
def show_lenta(request):
    return render(request, 'lenta.html', context={'posts': Post.objects.all()})

@csrf_exempt
def detail_post(request, pk):
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        return HttpResponse('Does Not Exist!', status=404)
    if request.method == 'GET':
        return render(request, 'detail-post.html', context={'post': post, 'comments': Comment.objects.all()})
    if request.method == 'POST':
        data = request.POST
        comment = Comment.objects.create(
            post = post, text = data['text']
        )
        return render(request, 'detail-post.html', context={'post': post, 'comments': Comment.objects.all()})

@csrf_exempt
def edit_post(request, pk):
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        return HttpResponse('Does Not Exist!', status=404)

    if request.method == 'GET':
        return render(request, 'edit-post.html', context={'post': post})
    if request.method == 'POST':
        data = request.POST
        if 'title' in data:
            post.title = data['title']
        if 'image' in data:
            post.image = data['image']
        if 'description' in data:
            post.description = data['description']

        post.save()
        return render(request, 'detail-post.html', context={'post': post})

@csrf_exempt
def delete_post(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return HttpResponse('Post deleted')

@csrf_exempt
def add_like(request):
    return HttpResponse(
        f"method: {request.method} </br> </br> header: {request.headers} </br> </br> body: {request.body}"
    )

