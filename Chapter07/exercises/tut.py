import numbers

def is_number(value):
    return isinstance(value, numbers.Number)

# Test cases
print(f"10 is a number: {is_number(10)}")
print(f"3.14 is a number: {is_number(3.14)}")
print(f"1 + 2j is a number: {is_number(1 + 2j)}")
print(f"'hello' is a number: {is_number('hello')}")
print(f"[1, 2, 3] is a number: {is_number([1, 2, 3])}")