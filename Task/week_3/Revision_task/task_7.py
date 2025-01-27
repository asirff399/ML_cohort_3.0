# Revision Task: 7. write a program to accept marks of 6 students and display them in a sorted manner and find out their average

marks = []

for i in range(6):
    mark = int(input(f'Enter the mark of student {i+1}: '))
    marks.append(mark)

sorted_marks = sorted(marks)
print("Sorted marks: ",sorted_marks)
average = sum(sorted_marks) / 6
print("Average mark: ",average)