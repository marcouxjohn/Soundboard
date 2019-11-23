class KeyConfig:
    def __init__(self):
        self.key_binds = {}

    def add_key_bind(self, key, sound_name):
        try:
            self.key_binds[key]
            return False
        except:
            self.key_binds[key] = sound_name
            return True

    def rem_key_bind(self, key):
        try:
            del self.key_binds[key]
            return True
        except:
            return True
