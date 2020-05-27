from django.shortcuts import render
from django.shortcuts import redirect
from community.forms import *

# Create your views here.
def write(request):
    if request.method =="POST":
        form = Form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.name = request.user
            post.save()
    else:
        form = Form()
    return render(request, 'community/write.html', {'form': form})

def list(request):
    articleList = reversed(Article.objects.all())
    return render(request, 'community/list.html', {'articleList':articleList})

def view(request, num):
    articleList = reversed(Article.objects.all())
    article = Article.objects.get(id = num)
    return render(request, 'community/view.html', {'articleList':articleList, 'article': article})
