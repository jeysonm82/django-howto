from django import apps
from django.core.urlresolvers import reverse

class AppConfig(apps.AppConfig):
    name = "apps.templates_basic"
    verbose_name = "Templates basic usage"
    files = ('urls.py','views.py')
    links = None
    description = "How to use templates (basic)."

    def ready(self):
        links = []
        links.append(("Basic", reverse('basic_template')))
        self.links = links


default_app_config = 'apps.templates_basic.AppConfig'
