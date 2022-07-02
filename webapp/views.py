from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import Article
from webapp.forms import ArticleForm


def index_view(request):
    articles = Article.objects.filter(status="active").order_by("-created_at")
    context = {"articles": articles}
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


# def update_article(request, pk):
#     article = get_object_or_404(Article, pk=pk)
#     if request.method == "GET":
#         form = ArticleForm(initial={
#             "title": article.title,
#             "author": article.author,
#             "content": article.content
#         })
#         return render(request, "update.html", {"form": form})
#     else:
#         form = ArticleForm(data=request.POST)
#         if form.is_valid():
#             article.title = form.cleaned_data.get("title")
#             article.author = form.cleaned_data.get("author")
#             article.content = form.cleaned_data.get("content")
#             article.save()
#             return redirect("article_view", pk=article.pk)
#         return render(request, "update.html", {"form": form})


def delete_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect("index")
