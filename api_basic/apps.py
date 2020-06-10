from django.apps import AppConfig


class ApiBasicConfig(AppConfig):
    name = 'api_basic'

    def ready(self):
        import api_basic.signals