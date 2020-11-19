from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms
from . models import Articles

#from . models import Post

# Create your views here.
def article_views(request):
    articles = Articles.objects.all().order_by('date')     
    return render(request, 'blog/create_article.html', {'art':articles})

@login_required(login_url='blog/loginuser')
def create_article(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES) 
        if form.is_valid():
            #save article to db
            echelon = form.save(commit=False)
            echelon.author = request.user
            echelon.save()
            return redirect('articles:article')
    else:
        form = forms.CreateArticle()
    return render(request, 'blog/single-blog.html', {'form':form})

#def blog(request):
    #post_item = Post.object.all()
    #return render(request, 'blog/single-blog.html',{'item':post_item})

def article_details(request, slug):
    article = Articles.objects.get(slug=slug)
    return render(request, 'blog/single_page.html', {'arts':article})