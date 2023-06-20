# Write a function that groups a string into parentheses clusters. Each cluster should be balanced.
#
# Examples
# split("()()()") ➞ ["()", "()", "()"]
#
# split("((()))") ➞ ["((()))"]
#
# split("((()))(())()()(()())") ➞ ["((()))", "(())", "()", "()", "(()())"]
#
# split("((())())(()(()()))") ➞ ["((())())", "(()(()()))"]

def split(str):
    clusters = []
    start = 0
    count = 0
    for i, char in enumerate(str):
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1

            if count == 0:
                clusters.append(str[start:i + 1])
                start = i + 1
    return clusters


print(split("()()()"))
print(split("((()))"))
print(split("((()))(())()()(()())"))
print(split("((())())(()(()()))"))
