from django.apps import DjangoApps
from django.contrib.sites.models import Site

class TodoApplication(DjangoApps):
    name = 'todo'
    verbose_name = 'Todo Application'

    def ready(self):
        if not Site.objects.exists():
            Site.objects.create(domain='localhost', name='localhost')