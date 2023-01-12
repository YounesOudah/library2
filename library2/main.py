from library2.Author import Author
from library2.Book import Book
from library2.library import library

aut1 = Author ("ahmed", "5656121", "ahmed.com")
aut2 = Author ("samy", "6656121", "samy.com")
aut3 = Author ("ali", "3356121", "ali.com")


book1 = Book("Java", "09-09-2009",1, aut1.id)
book2 = Book("Python", "10-10-2010", 2, aut2.id)
book3 = Book("PHP", "11-11-2011", 3, aut3.id)
book4 = Book("c#", "12-12-2012",4, aut2.id)

lib = library()

lib.add_author(aut1)
lib.add_author(aut2)
lib.add_author(aut3)

lib.add_book(book1)
lib.add_book(book2)
lib.add_book(book3)
lib.add_book(book4)

# for author in lib.Author :
#     print("name : " , author.name , "phone : " , author.phone, "Email : ", author.Email )

lib.print_author_books(aut2.id)