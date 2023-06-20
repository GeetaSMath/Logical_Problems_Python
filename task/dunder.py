class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __getitem__(self, index):
        if isinstance(index, int) and 0 <= index < self.pages:
            return f"Chapter {index + 1}"
        else:
            raise IndexError("Invalid chapter index")

book = Book("Python Programming", "John Doe", 300)

print(book)

print(len(book))

print(book[5])

# Iterate over chapters
for chapter in book:
    print(chapter)
