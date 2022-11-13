from django.apps import AppConfig


class AppcoderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appcoder'

def nueva_funcion_loca():
    print("Nueva funcion re loquita!")