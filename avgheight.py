#Python Program to find average height of people
#Let's Rock

height = input("Please enter heights of all students in single line separated by space. ").split()
print(height)
cnt = 0
ht = 0
total_ht = 0
for ht in height:
#    print(ht)
    cnt += 1
#    curr_ht = int(ht)
    total_ht += int(ht)
#    print(prev_ht)
print(f"There are {cnt} students and their average height is {round(total_ht/cnt)}")