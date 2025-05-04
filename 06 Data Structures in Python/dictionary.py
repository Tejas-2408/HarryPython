# student = {
#     "name":"Tejas",
#     "marks": 99,
#     "age":23
# }

# print(student)

# print(student['name'])

# student['marks'] = 100
# print(student)


marks = {"Tejas":100,"Ravi":99,"Ram":90}

print(marks.keys())
print(marks.values())
# marks.clear()  # clear the dictionary
marks.pop("Ram")
print(marks)


## Dictonary Comprehension

table_of_5 = {i:5*i for i in range(1,11)}
print(table_of_5)