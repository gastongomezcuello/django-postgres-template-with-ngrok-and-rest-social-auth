import requests

from django.core.management.base import BaseCommand
from dotenv import dotenv_values, set_key


class Command(BaseCommand):
    help = "get ngrok url and update ALLOWED_HOSTS in .env file"

    def handle(self, *args, **kwargs):

        try:
            response = requests.get("http://127.0.0.1:4040/api/tunnels")
            response.raise_for_status()
            data = response.json()
            public_url = data["tunnels"][0]["public_url"]
            ngrok_url = public_url.split("://")[1]

            env_path = ".env"
            env_values = dotenv_values(env_path)

            current_allowed_hosts = env_values.get(
                "ALLOWED_HOSTS", "localhost,127.0.0.1"
            ).split(",")

            if ngrok_url not in current_allowed_hosts:
                current_allowed_hosts.append(ngrok_url)

            set_key(env_path, "ALLOWED_HOSTS", ",".join(current_allowed_hosts))
            self.stdout.write(
                f"ALLOWED_HOSTS actualizado en .env: {','.join(current_allowed_hosts)}"
            )

            set_key(env_path, "BASE_URL", f"https://{ngrok_url}")
            self.stdout.write(f"BASE_URL actualizado en .env: https://{ngrok_url}")

        except Exception as e:
            self.stderr.write(f"Error al obtener la URL de Ngrok: {e}")
