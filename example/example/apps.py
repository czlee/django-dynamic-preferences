from django.apps import AppConfig

from dynamic_preferences.registries import preference_models
from .registries import my_model_preferences_registry

class ExampleAppConfig(AppConfig):
    name = 'example'

    def ready(self):
        MyPreferenceModel = self.get_model('MyPreferenceModel')
        preference_models.register(MyPreferenceModel, my_model_preferences_registry)
