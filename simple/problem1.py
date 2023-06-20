# Given an integer array, in-place reverse it without using any inbuilt functions.
#
# Input : Given an integer array, in-place reverse it without using any inbuilt functions.

# Input : [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]

def reverse_array(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        # Swap elements at start and end positions
        arr[start], arr[end] = arr[end], arr[start]

        # Increment start and decrement end
        start += 1
        end -= 1

# Example usage
arr = [1, 2, 3, 4, 5]
reverse_array(arr)
print(arr)  # Output: [5, 4, 3, 2, 1]
