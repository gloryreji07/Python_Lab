from typing import Dict, Optional, List

library: Dict[str, Dict[str, Optional[str]]] = {}

def add_book(isbn: str, title: str, author: str, publisher: str, volume: Optional[str], year: str) -> None:
   
    if isbn in library:
        raise ValueError(f"Book with ISBN {isbn} already exists.")
    library[isbn] = {
        'title': title,
        'author': author,
        'publisher': publisher,
        'volume': volume,
        'year': year
    }

def remove_book(isbn: str) -> None:
    if isbn not in library:
        raise ValueError(f"Book with ISBN {isbn} does not exist.")
    del library[isbn]

def get_book_details(isbn: str) -> Dict[str, Optional[str]]:
    if isbn not in library:
        raise ValueError(f"Book with ISBN {isbn} does not exist.")
    return library[isbn]

def search_books(search_term: str) -> List[Dict[str, Optional[str]]]:
    results = []
    for book in library.values():
        if search_term.lower() in book['title'].lower() or search_term.lower() in book['author'].lower():
            results.append(book)
    return results

def list_books() -> List[Dict[str, Optional[str]]]:
    return list(library.values())

def update_book(isbn: str, **kwargs) -> None:
    if isbn not in library:
        raise ValueError(f"Book with ISBN {isbn} does not exist.")
    
    for key, value in kwargs.items():
        if key in library[isbn]:
            library[isbn][key] = value

def check_availability(isbn: str) -> bool:
    return isbn in library
