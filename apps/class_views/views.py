from django.shortcuts import render

# Create your views here.
from django.views.generic import View, TemplateView
from django.http import HttpResponse
"""
https://github.com/django/django/blob/master/django/views/generic/base.py
"""

class BasicView(View):

    """                                                   ----> View.get()
                                                          |
    URL dispatcher -> View.as_view() -> View.dispatch() --|
                                                          ----> View.post()
    """
    trace = ''

    @classmethod
    def as_view(cls, **initargs):
        cls.trace += "as_view() ---> "
        return super(BasicView, cls).as_view(**initargs)

    def dispatch(self, *args, **kwargs):
        self.trace += "dispatch() ---> "
        return super(BasicView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.trace += "get()"
        return HttpResponse("GET <br/>" + self.trace + "<br/> Data: %s"%(request.GET['var']))

    def post(self, request, *args, **kwargs):
        self.trace += "post()"
        return HttpResponse("POST <br/>" + self.trace)


class TemplateViewSample(TemplateView):
    template_name = "class_views/sample.html"

    def get_context_data(self, **kwargs):
        context = super(TemplateViewSample,self).get_context_data(**kwargs)
        import time
        context['data'] = time.time()
        return context
