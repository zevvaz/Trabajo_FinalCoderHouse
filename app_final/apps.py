from django.apps import AppConfig


class app_finalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_final'
    
    def ready(self):
        import app_final.signals
    
    


