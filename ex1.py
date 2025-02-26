# EXERCICE 1

class Section:
    def __init__(self, **kargs):
        self.elements = kargs

    def get_field(self, name):
        return self.elements.get(name, None)

    def set_field(self, name, value):
        self.elements[name] = value

class Singleton:
    def get_instance(self):
        return None

class Config (Singleton):
    _config = None

    def define_config(config: Section):
        Config._config = config

    def get_instance():
        return Config._config

### CODE EXEMPLE
if __name__ == '__main__':
    cfg = Section(
            gameplay = Section(difficulte = "Normale", langue = "FR"),
            audio = Section(vol_musique = 50, vol_sfx = 80),
            graphics = Section(reso = "1920x1080", qual = "RTX Raytracing Ultra-high Definition Graphics with AI upscaling"))
    
    Config.define_config(cfg)

    # Obtention de la configuration a l'aide du Singleton
    config_singleton = Config.get_instance()

    assert cfg == config_singleton
