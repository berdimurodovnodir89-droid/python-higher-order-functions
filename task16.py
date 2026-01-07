data = [123, "apple", "banana", "cat", 456, "mango", "elephant"]

result = filter(
    lambda x :
    type(x) == str and len(x) > 5,
    data
)

print(list(result))