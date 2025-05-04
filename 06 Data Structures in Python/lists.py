# # marks = [12,23,34,56,67,78]
# # mixed = ["tejas",23,9.47]

# # print(marks)
# # print(mixed)
# # print(marks[0])
# # print(marks[2:4])

# marks = [12,23,345,45]

# print(marks)
# marks.append(54)
# print(marks)
# marks.pop()
# print(marks)


## List Comprehension

a = 5 
table = []

for i in range(1,11):
    table.append(a*i)

print(table)

t = [5*i for i in range(1,11)]
print(t)