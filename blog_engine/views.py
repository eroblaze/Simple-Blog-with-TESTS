from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogModel
from django.urls import reverse_lazy


def index(request):
    all_blogs = BlogModel.objects.all().order_by("-id")
    return render(request, 'index.html', {"all_blogs": all_blogs})

def post(request, pk):
    post = get_object_or_404(BlogModel, pk=pk)
    return render(request, 'post.html', {'post': post})

def create(request):
    if request.method == 'POST':
        heading = request.POST.get('heading')
        content = request.POST.get('content')
        
        new_post = BlogModel(Heading=heading, body=content)
        new_post.save()
        return redirect(f"/post/{new_post.id}/") 
    else:
        return render(request, 'createpost.html')

def delete_all(request):
    BlogModel.objects.all().delete()
    return redirect(reverse_lazy(index))