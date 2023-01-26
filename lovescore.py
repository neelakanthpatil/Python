#Python Program to calculate your Love Score
#let's Rock

print("Welcome to the Love Calculator...!!!")
name1 = input("Whats Your Name ? ")
name2 = input("Whats their Name ? ")

#name1_low = name1.lower()
#name2_low = name2.lower()

name = name1 + name2
final_name = name.lower()

t_count = final_name.count("t")
r_count = final_name.count("r")
u_count = final_name.count("u")
e_count = final_name.count("e")
l_count = final_name.count("l")
o_count = final_name.count("o")
v_count = final_name.count("v")

count1 = t_count + r_count + u_count + e_count
count2 = l_count + o_count + v_count + e_count

final_count = str(count1) + str(count2)

#print(final_count)

int_final_count = int(final_count)
if int_final_count < 10 or int_final_count > 90:
    print(f"Your Score is {int_final_count}, you go together like coke and mentos.")
elif int_final_count >= 40 and int_final_count <= 50:
    print(f"your score is {int_final_count}, you are alright together.")
else:
    print(f"your score is {int_final_count}")