from django.apps import AppConfig


class CakeAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cake_app'

    def ready(self):
        import cake_app.signals
