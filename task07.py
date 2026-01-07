prices = ["$120", "$340", "$50", "$90"]
num = map(lambda num : num.replace("$",""),prices)

print(list(num))