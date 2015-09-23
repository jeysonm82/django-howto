from django.shortcuts import render
from django.conf import settings
from django.apps import apps
import os
# Create your views here.

def home(request):
    l = [apps.get_app_config(x.split(".")[-1]) for x in settings.EXAMPLE_APPS]
    return render(request, "browser/home.html",{'apps_list': l})

def view_example(request, app_name):
    app = apps.get_app_config(app_name.split(".")[-1])
    files =   [(x, _read_contents(app.path + '/' +x)) for x in app.files]
    links = [x for x in app.links]
    return render(request, "browser/view.html",{'app': app,'files': files , 'links': links})

def _read_contents(path):
    with open(path, 'r') as f:
        out = f.read()
    return out
