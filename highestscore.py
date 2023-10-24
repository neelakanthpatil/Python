#Python program to find the highest score in a array/list
#Let's Python

marks = input("Enter marks for all students separated by space. ").split()
print(marks)
#marks_list = [marks]
prev_mark = 0
for mark in marks:
    curr_mark = int(mark)
    if prev_mark < curr_mark:
        prev_mark = curr_mark
print(f"The highest score in the class is : {prev_mark}")

