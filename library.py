class Library():

    def __init__(self,books: list,loans: list):
        self.__books = books
        self.__loans = loans

    def __str__(self):
        return f'Books: {self.__books}\nLoans: {self.__loans}'

    @property
    def books(self):
        return self.__books
    
    def books(self,booksList:list):
        # check if the parameter's value is from list type
        if isinstance(booksList,list):
            self.__livros = booksList
        else:
            raise
        ValueError('Invalid type! The parameter must be of type list.')

    
    @property
    def loans(self):
        return self.__loans

    def loans(self,loansList:list):
        # check if the parameter's value is from list type
        if isinstance(loansList,list):
            self.__loans = loansList
        else:
            raise
        ValueError('Invalid type! The parameter must be of type list.')



# library = Library(['teste1','teste2'],['teste3','teste4'])
# print(library)

       
    
