from django.shortcuts import render


def basic(request):
    return render(request, "templates_basic/basic.html")
