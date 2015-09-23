from django import apps
from django.core.urlresolvers import reverse

class AppConfig(apps.AppConfig):
    name = "apps.url_routing"
    verbose_name = "URL routing"
    files = ('urls.py','views.py')
    links = None
    description = "How to work with URL Dispatcher."

    def ready(self):
        links = []
        links.append(("Single", reverse('single')))
        links.append(("4 digits", reverse('4 digits', args=(2015,))))
        links.append(("4 and 2 digits", reverse('4 and 2 digits', args=(2015, 16))))
        links.append(("Any", reverse('Arbitrary digits', args=(123456,))))
        self.links = links


default_app_config = 'apps.url_routing.AppConfig'
