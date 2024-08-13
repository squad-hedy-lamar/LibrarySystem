# Corrigindo a estrutura do dicionário de livros
books = [
    {'name': 'A Fúria dos Reis', 'genre': 'Suspense', 'description': 'Livro de suspense medieval'},
    {'name': 'Quarto dos Reis', 'genre': 'Terror', 'description': 'Livro de terror e guerras medievais'},
    {'name': 'Querido John', 'genre': 'Romance', 'description': 'História de romance'},
    {'name': 'Muquerela', 'genre': 'Infantojuvenil', 'description': 'História infantil, abordando birras'}
]

# Classe para representar um livro
class Book:
    def __init__(self, name, genre, description):
        self.name = name
        self.genre = genre
        self.description = description

# Classe para representar um gênero
class Genre:
    def __init__(self, genre_name):
        self.genre_name = genre_name
        self.books = []

    def add_book(self, book):
        if book.genre.lower() == self.genre_name.lower():
            self.books.append(book)

    def get_books(self):
        return [book.name for book in self.books]

# Criando instâncias de livros e adicionando ao gênero correspondente
suspense_genre = Genre('Suspense')
romance_genre = Genre('Romance')  # Corrigido o nome do gênero
terror_genre = Genre('Terror')
infanto_genre = Genre('Infantojuvenil')

for book_data in books:
    book = Book(book_data['name'], book_data['genre'], book_data['description'])
    if book.genre.lower() == 'suspense':
        suspense_genre.add_book(book)
    elif book.genre.lower() == 'terror':
        terror_genre.add_book(book)
    elif book.genre.lower() == 'romance':
        romance_genre.add_book(book)
    elif book.genre.lower() == 'infantojuvenil':
        infanto_genre.add_book(book)

# Testando o código
print(f"Livros de suspense: {suspense_genre.get_books()}")
print(f"Livros de terror: {terror_genre.get_books()}")
print(f"Livros de romance: {romance_genre.get_books()}")
print(f"Livros infantojuvenil: {infanto_genre.get_books()}")
