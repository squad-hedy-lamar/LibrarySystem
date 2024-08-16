class User(Person):
    def __init__(self, id: int, name: str, phone: str, nationality: str):
        # Chamando o construtor da classe mãe (Person)
        super().__init__(id, name, phone, nationality)
