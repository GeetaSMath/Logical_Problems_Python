# my_list = [1, 2, 3]
# my_iter = iter(my_list)
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
#
#
# def my_generator():
#     yield 1
#     yield 2
#     yield 3
#
# gen = my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# class MyIterator:
#     def __init__(self, data):
#         self.data = data
#         print(data,"input")
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index >= len(self.data):
#             raise StopIteration
#         value = self.data[self.index]
#         print(value,"value")
#         self.index += 1
#         return value
#
#
# # Example usage:
# my_list = [1, 2, 3, 4, 5]
# my_iter = MyIterator(my_list)
#
# for item in my_iter:
#     print(item)


# example using iterator
my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list)

while True:
    try:
        item = next(my_iter)
        print(item, "using iterator")
    except StopIteration:
        break

my_list = [1, 2, 3, 4, 5]

for item in my_list:
    print(item, "without using iterator")


# without using iterator
class Squares:
    def __init__(self, n):
        self.n = n

    def generate_squares(self):
        for num in range(self.n):
            square = num ** 2
            yield square


# Example usage:
squares = Squares(5)

for square in squares.generate_squares():
    print(square)


# using iterator
class Squares:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.n:
            raise StopIteration
        square = self.current ** 2
        self.current += 1
        return square


# Example usage:
squares_iter = Squares(5)

for square in squares_iter:
    print(square, "square number")
