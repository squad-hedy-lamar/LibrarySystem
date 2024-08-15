#import da outra classe que será implementada
from person import Person

class Author(Person):
    def __init__(self, name, phone, nationality):
        super().__init__(name, phone, nationality)