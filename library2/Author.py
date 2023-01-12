class Author :

    __id_author = 0

    def __init__(self , name , phone , Email):
        Author.__id_author += 1
        self.id = Author.__id_author
        self.name = name
        self.phone = phone
        self.Email = Email


aut1 = Author("ahmad 1", "5120521", "ahmad.com")
aut2 = Author("ahmad 2", "5120521", "ahmad.com")
aut3 = Author("ahmad 3", "5120521", "ahmad.com")
aut4 = Author("ahmad 4", "5120521", "ahmad.com")


