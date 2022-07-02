from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import Article
from webapp.forms import ArticleForm, ArticleSearch


def index_view(request):
    form = ArticleSearch()

    if request.method == 'GET' and 'authorName' in request.GET:
        authorName = request.GET['authorName']
        articles = Article.objects.filter(authorName=authorName)
    else:
        articles = Article.objects.filter(status="active").order_by("-created_at")
    context = {"articles": articles, "form": form}
    return render(request, "index.html", context)


def create_article(request):
    if request.method == "GET":
        form = ArticleForm()
        return render(request, "create.html", {"form": form})
    else:
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            author_name = form.cleaned_data.get("authorName")
            author_email = form.cleaned_data.get("authorEmail")
            content = form.cleaned_data.get("content")
            Article.objects.create(authorName=author_name, authorEmail=author_email, content=content)
            return redirect("index")
        return render(request, "create.html", {"form": form})


def update_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "GET":
        form = ArticleForm(initial={
            "authorName": article.authorName,
            "authorEmail": article.authorEmail,
            "content": article.content
        })
        return render(request, "update.html", {"form": form})
    else:
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article.authorName = form.cleaned_data.get("authorName")
            article.authorEmail = form.cleaned_data.get("authorEmail")
            article.content = form.cleaned_data.get("content")
            article.save()
            return redirect("index")
        return render(request, "update.html", {"form": form})


def delete_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "GET":
        pass
        return render(request, "delete.html", {"article": article})
    else:
        article.delete()
        return redirect("index")
