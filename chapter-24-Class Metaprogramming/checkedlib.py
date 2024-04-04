class Plugin:
    _plugins = []  # Registry for subclasses

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls._plugins.append(cls)  # Register the subclass

    @classmethod
    def get_plugins(cls):
        return cls._plugins


