
_spoken = []


def get_spoken():
    return _spoken


class Sound(object):
    def speak(self, text):
        _spoken.append(text)
