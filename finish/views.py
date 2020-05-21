from django.shortcuts import render
from django.http import HttpResponse
from .crawling import danggn
from .crawling import imageurl

def form_test(request):
    if request.method == "GET":
        return render(request, "index.html")
    elif request.method == "POST":
        search = request.POST["search"]
        title = danggn(search)
        imgurl = imageurl(search)
        return render(request, "index.html", context={"title": title, "imgurl": imgurl})


def login(request):
    context = {

    }
    return render(request, "login.html", context=context)


def all_views(request, search):
    return render(request, "f_template.html", context={"title": title})
