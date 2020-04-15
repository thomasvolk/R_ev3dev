
_spoken = []


def get_spoken():
    return _spoken


def clear_spoken():
    _spoken.clear()


class Sound(object):
    def speak(self, text):
        _spoken.append(text)
