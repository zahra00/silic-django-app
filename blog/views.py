from django.shortcuts import render
from .models import Article
from django.http import HttpResponse, JsonResponse


def index(request):
    return HttpResponse("some thing")


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
    return render(request, 'test.html', context)


def list_all_article(request):
    context = {
        "Articles": Article.objects.all()
    }
    return render(request, 'home.html', context)


def detail_article(request, slug):
    context = {
        "article": Article.objects.get(slug=slug)
    }
    return render(request, 'detail.html', context)
