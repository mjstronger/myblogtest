from django.shortcuts import render
from django.http import HttpResponse
import json


from . import models

# from .models import Article

# def index(request):
#     articles = models.Article.objects.all()
#     return render(request,'index.html',{'articles':articles})

def index(request):
    return render(request, 'index.html')

# def article_page(request,article_id):
#     article = models.Article.objects.get(pk=article_id)
#     return render(request, 'article_page.html', {'article': article})

# def edit_page(request,article_id):
#     if str(article_id) == '0':
#         return render(request, 'edit_page.html')
#     article = models.Article.objects.get(pk=article_id)
#     return render(request,'edit_page.html', {'article': article})

def delete(request,article_id):
    article = models.Article.objects.get(pk=article_id)
    article.delete()
    return HttpResponse("<p>删除成功<p>")

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    models.Article.objects.create(title=title, content=content)
    return HttpResponse('success')

def update(request):
    id = request.POST.get('id')
    title = request.POST.get('title')
    content = request.POST.get('content')
    blog_up = models.Article.objects.get(id=int(id))
    blog_up.title = title
    blog_up.content = content
    blog_up.save()

def get_date(request):
    id = request.POST.get('id')
    if id:
        id = int(id)
        blogs = models.Article.objects.filter(id=id)
    else:
        blogs = models.Article.objects.all()
    blog_items =[]
    for blog in blog_items:
        blog_items.append({'title': blog.title, 'content': blog.content, 'id': blog.id,})
    return HttpResponse(json.dumps(blog_items))

def search(request):
    pass