from django import apps
from django.core.urlresolvers import reverse

class AppConfig(apps.AppConfig):
    name = "apps.class_views"
    verbose_name = "Class based views (Basic)"
    files = ('urls.py','views.py')
    links = None
    description = "How to use class based views (basic)"

    def ready(self):
        links = []
        links.append(("Basic (GET)", reverse('class_based_views')+"?var=10"))
        links.append(("Basic (POST)", reverse('class_based_views')))
        links.append(("Basic Template", reverse('class_based_views_template')))
        self.links = links


default_app_config = 'apps.class_views.AppConfig'
