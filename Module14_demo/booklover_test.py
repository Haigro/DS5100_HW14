import unittest
from booklover import BookLover

import pandas as pd

class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        actual = BookLover('Jose', 'jyd2hw@gmail.com', 'Horror')
        actual.add_book('Frankenstein', 4)
        self.assertTrue(actual.book_list['book_name'].str.contains('Frankenstein').any())

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        actual = BookLover('Jose', 'jyd2hw@gmail.com', 'Horror')
        actual.add_book('Frankenstein', 4)
        actual.add_book('Frankenstein', 4)
        self.assertEqual(list(actual.book_list["book_name"]).count("Frankenstein"), 1)

    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        actual = BookLover('Jose', 'jyd2hw@gmail.com', 'Horror')
        actual.add_book('Frankenstein', 4)
        self.assertTrue(actual.has_read('Frankenstein'))

    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`  
        actual = BookLover('John', 'Johnners@gmail.com', 'Scifi')
        self.assertFalse(actual.has_read('Moby Dick'))

    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        actual = BookLover('John', 'Johnners@gmail.com', 'Scifi')
        expected = 3
        actual.add_book('War of the Worlds', 4)
        actual.add_book('Percy Jackson', 4)
        actual.add_book('Harry Potter', 4)
        self.assertEqual(actual.num_books, expected)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        actual = BookLover('Jose', 'jyd2hw@gmail.com', 'Horror')
        expected = 1
        actual.add_book('Moby Dick', 4)
        actual.add_book('Twilight', 2)
        actual.add_book('To Kill a Mockingbird', 3)
        self.assertEqual(len(actual.fav_books()), expected)

if __name__ == '__main__': 

    unittest.main(verbosity=3)