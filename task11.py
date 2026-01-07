nums = list(range(1, 21))

result = list(filter(
    lambda x : x % 2 == 0 ,nums
))
total = list(map(
    lambda x : x ** 2 , result
))

print(result)
print(total)