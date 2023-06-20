#what is generator
#WHY WE NEED IT
#HOW TO USE ,WHEN TO USE
#SYNTAX OF THAT


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Example usage:
fib_gen = fibonacci()

# Generate and print the first 10 Fibonacci numbers
for _ in range(10):
    print(next(fib_gen))


#without using generator
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Example usage:
fib_sequence = fibonacci(10)

# Print the Fibonacci sequence
for num in fib_sequence:
    print(num)
