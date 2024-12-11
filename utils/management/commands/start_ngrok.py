import os
import platform
import subprocess
from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = (
        "create configuration file for ngrok and run ngrok with the configuration file"
    )

    def handle(self, *args, **options):

        ngrok_path = os.path.join(settings.BASE_DIR, "ngrok.yml")
        with open(ngrok_path, "w") as f:
            f.write(
                f"""
version: '3'
agent:
    authtoken: {settings.NGROK_AUTHTOKEN}
tunnels:
    django:
        proto: http
        addr: 8000
        inspect: false
            """
            )

        system = platform.system()
        if system == "Windows":
            subprocess.Popen(f'ngrok start --config "{ngrok_path}" django', shell=True)
        else:
            subprocess.Popen(f'ngrok start --config "{ngrok_path}" django', shell=True)

        self.stdout.write(self.style.SUCCESS("ngrok is running"))
