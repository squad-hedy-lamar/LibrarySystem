class Copy:
    def __init__(self, code: str):
        self.__code = code
        self.__borrowed = False

    @property
    def code(self):
        return self.__code

    @property
    def borrowed(self):
        return self.__borrowed

    @borrowed.setter
    def borrowed(self, value: bool):
        self.__borrowed = value
