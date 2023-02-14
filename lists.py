#Python program to print the values from the lists
#Let's Start

row1 = ["😀","😀","😀"]
row2 = ["😀","😀","😀"]
row3 = ["😀","😀","😀"]
map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put a Treasure ? ")
#print(position)
#print(map[0][0])
ind1 = int(position[0]) - 1
ind2 = int(position[1]) - 1
#print(ind1)
#print(ind2)

map[ind2][ind1] = 'X'
print(f"{map[0]}\n{map[1]}\n{map[2]}")
