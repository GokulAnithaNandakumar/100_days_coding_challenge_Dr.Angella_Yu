# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
horizontal=int(position[0])    #Here horizontal 0 and vertical 1 specifies the posion if we type 23 the horizontal is 2 and vertical is 3 horizontal in 0 position vertical in 1 position
vertical=int(position[1])
map[vertical-1][horizontal-1]="X"



#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
