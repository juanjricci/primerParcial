from repository import Repository
from book import Book


class BookService:

    def add_book(self, book):
        bookKey = -1
        for key in Repository.booksList:
            bookKey = key
        bookKey = bookKey + 1
        Repository.booksList[bookKey] = book.__dict__

    def update_book(self, key, book):
        if key in Repository.booksList:
            Repository.booksList[key] = book.__dict__
        else:
            raise ValueError('No existe legajo')

    def delete_book(self, key):
        del Repository.booksList[key]

    def assign_book(self, book_id, member_legajo):
        if book_id in Repository.booksList.keys():
            pass
        else:
            raise ValueError('No existe legajo')
        if member_legajo in Repository.booksList:
            pass
        else:
            raise ValueError('No existe legajo')
        pass
