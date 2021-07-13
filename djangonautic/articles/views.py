from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

from .models import Article

# Create your views here.


def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, "articles/article_list.html", {'articles_to_show': articles})


def article_detail(request, slug):
    # return HttpResponse(slug)
    single_article_detail = Article.objects.get(slug=slug)

    return render(request, 'articles/article_detail.html', {'article': single_article_detail})
