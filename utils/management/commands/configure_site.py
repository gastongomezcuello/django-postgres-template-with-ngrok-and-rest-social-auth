import os
from django.core.management.base import BaseCommand
from django.contrib.sites.models import Site


class Command(BaseCommand):
    help = "set up the site domain and name in the database"

    def handle(self, *args, **kwargs):
        app_domain = os.getenv("BASE_URL", default="http://localhost:8000")
        my_app_name = os.getenv("APP_NAME", default="My App")
        site, created = Site.objects.get_or_create(id=1)
        site.domain = app_domain
        site.name = my_app_name
        site.save()
        if created:
            self.stdout.write(
                self.style.SUCCESS(f"New site created: {app_domain}")
            )
        else:
            self.stdout.write(self.style.SUCCESS(f"Site updated to: {app_domain}"))
