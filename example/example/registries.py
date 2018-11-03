from dynamic_preferences.registries import PerInstancePreferenceRegistry


class MyModelPreferenceRegistry(PerInstancePreferenceRegistry):
    pass


my_model_preferences_registry = MyModelPreferenceRegistry()
