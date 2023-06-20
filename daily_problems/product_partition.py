def can_partition(lst):
    total_product = 1
    for num in lst:
        total_product *= num
    for num in lst:
        if num != 0 and total_product % num == 0 and total_product // num == num_product(lst, num):
            return True

        return False


def num_product(lst, num):
    product = 1
    for n in lst:
        if n != num:
            product *= n
    return product


print(can_partition([2, 8, 4, 1]))
print(can_partition([-1, -20, 5, -1, -2, 2]))
