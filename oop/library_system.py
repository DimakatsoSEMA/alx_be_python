class Book:
   def __init__(self, title, author):
       self.title = title
       self.author = author
   def get_details(self):
       return f"Title: {self.title}, Author: {self.author}"


class Ebook(Book):
    def __init__(self, title, author, file_name): 
        super().__init__(title, author)
        self.file_name = file_name
    def get_details(self):
        return f"{super().get_details()}, File Size: {self.file_size}MB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count
    def get_details(self):
        return f"{super().get_details()}, Pages: {self.page_count}"


class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Only Book instances can be added.")



