from django.apps import AppConfig


class UserManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_management'

    def ready(self) -> None:
        from signals import my_signals
        return super().ready()
