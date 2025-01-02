# Using Constructor with Default Arguments
class Book:
    def __init__(self, title, author="Unknown"):
        self.title = title
        self.author = author

book1 = Book("1984")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
print(f"Book 1: {book1.title} by {book1.author}")
print(f"Book 2: {book2.title} by {book2.author}")

# Multiple Instance Variables
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

rect = Rectangle(5, 10)
print(f"Rectangle has width {rect.width} and height {rect.height}")