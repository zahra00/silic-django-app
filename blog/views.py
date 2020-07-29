from django.shortcuts import render, get_object_or_404
from .models import Article
from django.http import HttpResponse, JsonResponse


def index(request):
    return render(request, 'home.html')


def json(request):
    data = {
        "1": {
            "name": "st1",
            "mode": "sad"
        },
        "2": {
            "name": "st2",
            "mode": "happy"
        }
    }
    return JsonResponse(data)


def template(request):
    context = {

        "students": [
            {
                "name": "st1",
                "mode": "dep"
            },
            {
                "name": "st2",
                "mode": "sad"
            },
            {
                "name": "st3",
                "mode": "happy"
            },
        ]

    }
    return render(request, 'about.html', context)


def list_all_article(request):
    context = {
        "Articles": Article.objects.all()
    }
    return render(request, 'home.html', context)


def detail_article(request, slug):
    context = {
        "article": get_object_or_404(Article, slug=slug, status="p")
    }
    return render(request, 'post.html', context)
