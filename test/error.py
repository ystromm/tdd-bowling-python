class SomeError(Exception):
    def __init__(self, message):
        self.message = message


def raises_some_error():
    raise SomeError("Everything is borken")