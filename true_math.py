from math import inf

def divide(first, second):
    if second == 0:
        return inf
    else:
        first / second

print(divide(49, 7))
print(divide(15, 0))


