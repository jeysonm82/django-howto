from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import resolve

# Create your views here.

def routing(request, *args, **kwargs):
    name = resolve(request.path).url_name
    return HttpResponse("""<ul>
    <li>Path: %s</li>
    <li>URL name: %s</li>
    <li>args: %s</li>
    <li>kwargs: %s</li>
    </ul>"""%(request.path, name, args, kwargs))
