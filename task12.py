students = [
  {"name": "Aziz", "grade": 89},
  {"name": "Kamola", "grade": 95},
  {"name": "Javlon", "grade": 76}
]

result = list(sorted(
    students,key = lambda grade: grade["grade"]
))

print(result)