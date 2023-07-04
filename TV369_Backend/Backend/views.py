from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User, NewsArticle

def create_user(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create(full_name=full_name, username=username, password=password)
        return HttpResponse('User created successfully!')
    return render(request, 'create_user.html')
def check_server(request):
    return HttpResponse("Server is running!")
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.get(username=username, password=password)
        if user:
            return HttpResponse('Login successful!')
        else:
            return HttpResponse('Invalid username or password!')
    return render(request, 'login.html')

def show_users(request):
    users = User.objects.all()
    return render(request, 'show_users.html', {'users': users})

def create_news_article(request):
    if request.method == 'POST':
        author = User.objects.get(username=request.POST['author'])
        title = request.POST['title']
        cover_image = request.FILES['cover_image']
        content = request.POST['content']
        categories = request.POST['categories']
        NewsArticle.objects.create(author=author, title=title, cover_image=cover_image, content=content, categories=categories)
        return HttpResponse('News article created successfully!')
    return render(request, 'create_news_article.html')

def show_10_news_articles(request):
    news_articles = NewsArticle.objects.order_by('-created_at')[:10]
    return render(request, 'show_news_articles.html', {'news_articles': news_articles})

def show_all_news_articles(request):
    news_articles = NewsArticle.objects.all()
    return render(request, 'show_news_articles.html', {'news_articles': news_articles})

def show_news_articles_by_category(request, category):
    news_articles = NewsArticle.objects.filter(categories=category).order_by('-created_at')[:10]
    return render(request, 'show_news_articles.html', {'news_articles': news_articles})
