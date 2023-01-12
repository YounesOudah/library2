class Book :

    __id_book = 0

    def __init__(self , title:str , publishing_date:str , version:int, id_author):
        Book.__id_book += 1
        self.id = Book.__id_book
        self.title = title
        self.publishing_date = publishing_date
        self.version = version
        self.id_author = id_author




