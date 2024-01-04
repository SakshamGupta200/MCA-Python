l1 = [('arjun', 21),
      ('arushi', 22),
      ('aman', 22),
      ('tanmai', 23)]

marks = []
for item in l1:
    marks.append(item[1])

marks = sorted(set(marks))
second_highest_marks = marks[1]

for item in l1:
    if item[1] == second_highest_marks:
        print(item[0])
