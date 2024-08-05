import LibraryManager as lm

def demonstrate_library_operations():
 
    lm.add_book('978-0134685991', 'Operating Systems: Three Easy Pieces', 'Remzi H. Arpaci-Dusseau', 'Arpaci-Dusseau', '1st', '2020')
    lm.add_book('978-0134685992', 'Introduction to Machine Learning with Python', 'Andreas C. Müller', 'O\'Reilly Media', '1st', '2021')
    lm.add_book('978-0134685993', 'Data Structures and Algorithm Analysis in Python', 'Clifford A. Shaffer', 'Cambridge University Press', '3rd', '2022')
    
    print("Initial Library:")
    print(lm.list_books())
    
    print("\nDetails of book with ISBN 978-0134685991:")
    print(lm.get_book_details('978-0134685991'))
    
    print("\nSearch results for 'Machine Learning':")
    print(lm.search_books('Machine Learning'))
    
    print("\nUpdating book with ISBN 978-0134685992...")
    lm.update_book('978-0134685992', volume='2nd', year='2023')
    print("Updated details of book with ISBN 978-0134685992:")
    print(lm.get_book_details('978-0134685992'))
    
    print("\nChecking availability of book with ISBN 978-0134685993:")
    print("Available" if lm.check_availability('978-0134685993') else "Not Available")
    
    print("\nRemoving book with ISBN 978-0134685993...")
    lm.remove_book('978-0134685993')
    print("Library after removal of the book with ISBN 978-0134685993:")
    print(lm.list_books())

if __name__ == "__main__":
    demonstrate_library_operations()
