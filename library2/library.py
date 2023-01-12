class library :
    Author = []
    Book = []

    def add_author(self, author):
        self.Author.append(author)

    def remove_author(self, id ):

        for author in self.Author :

            if author.id == id :
                self.Author.remove(author)

                return

            print("Author with id : " , id , "is not found")


    def print_author(self, id):
        for author in self.Author :
            if author.id == id :
                print("name : ", author.name, "phone : ", author.phone, "Email : ", author.Email)

                return
            print("Author with id : " , id , "is not found")

    def print_authors(self):

        for author in self.Author :

            print("name : ", author.name, "phone : ", author.phone, "Email : ", author.Email)


    def print_author_books(self, id):
        is_author_exist = False
        author_name = ""
        for author in self.Author :
            if author.id == id :
                is_author_exist = True
                author_name = author.name
                break

        if is_author_exist == False :
            print("Author with id : " , id , "is not found")
            return

        print("books of author " , author.name,  " : ",)
        for book in self.Book :
            if book.id_author == id :
                print("title : " , book.title)


    def add_book(self, book):
        self.Book.append(book)


    def remove_book(self, id):
        for book in self.Book:
            if book.id == id:
                self.Book.remove(book)
                return
        print("Book with id", id , "is not found!")

    def print_book(self, id):
        for book in self.Book:
            if book.id == id:
                print("Book with id", book.id , "information.")
                print("Title : ", book.title)
                print("Publishing_data : ", book.publishing_date)
                for author in self.Author :
                    if author.id == book.id_author :
                        print("Author : ", author.name )
                    return

        return
    print("Book with id", id , "is not found!")


    def print_books(self):
        for book in self.Book:
            print("Book with id",book.id , "information.")
            print("Title : ", book.title)
            print("Publishing_data : ", book.publishing_date)
            for author in self.Author:
                if author.id == book.id_author:
                    print("Author : ", author.name)
                    break
            print("_______________________________________\n")










