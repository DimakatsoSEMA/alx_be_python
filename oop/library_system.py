class Book:
   def __init__(self, title, author):
       self.title = title
       self.author = author

class Ebook(Book):
    def __init__(self, title, author, file_name): 
        super().__init__(title, author)
        self.file_name = file_name

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count



