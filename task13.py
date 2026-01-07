sentence = "Functional programming in Python is very powerful and elegant"
result = sentence.split()
total = sorted(
    result,key = lambda x : len(x),reverse=True
)
text_3 = total[:3]
print(text_3)