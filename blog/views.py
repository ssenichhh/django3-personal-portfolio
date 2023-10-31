from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blog.models import Project1

def all_blogs(request):
    projects = Project1.objects.order_by('-date')
    return render(request, 'blog/all_blogsnew.html', {'projects': projects})

def detail(request, blog_id):
    blog = get_object_or_404(Project1, pk=blog_id)
    return render(request, 'blog/detailnew.html', {'blog': blog})
