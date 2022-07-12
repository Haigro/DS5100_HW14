from Module14_demo import booklover

bl = booklover.BookLover("name","email","horror")
bl.add_book("Armaggedon",4)
print(bl.num_books_read())
