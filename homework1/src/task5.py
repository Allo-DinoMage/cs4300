def my_fav_books():
    #Here we initialize a list of books
    books = [
        "Frankenstein - Mary Shelley", 
        "Soul Eater - Atsushi Ohkubo", 
        "I'm The Grim Reaper - Graveweaver", 
        "Savage Worlds - Shane Lacy Hensley", 
        "Yu-Gi-Oh - Kazuki Takahashi"
    ]

    return books


def first_three_books():
    #Use list slicing to get first 3 books
    #grab the books
    books = my_fav_books()
    #slice the books
    first_three = books[:3] 
    return first_three


def student_database():
    #Create a dictionary of students and their IDs
    students = {
        "Alice": 12345,
        "Bob": 67890,
        "Charlie": 11111,
        "Diana": 22222
    }
    
    return students


if __name__ == "__main__":
    # Show the full book list
    print("My favorite books:")
    for book in my_fav_books():
        print(f"  - {book}")
    
    # Show first three using slicing
    print("\nFirst three books (using slicing):")
    for book in first_three_books():
        print(f"  - {book}")
    
    # Show student database
    print("\nStudent Database:")
    for name, student_id in student_database().items():
        print(f"  {name}: {student_id}")