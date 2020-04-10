

class Sound(object):
    def __init__(self):
        self.spoken = []

    def speak(self, text):
        self.spoken.append(text)
