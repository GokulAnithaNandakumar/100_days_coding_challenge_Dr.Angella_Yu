# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇





#Write your code above this row 👆

# 🚨 Don't change the code below 👇

if position=="11":
  row1[0]="X"
  print(f"{row1}\n{row2}\n{row3}")
elif position=="21":
  row1[1]="X"
  print(f"{row1}\n{row2}\n{row3}")
elif position=="31":
  row1[2]="X"
  print(f"{row1}\n{row2}\n{row3}")
elif position=="12":
  row2[0]="X"
  print(f"{row1}\n{row2}\n{row3}")
elif position=="22":
  row2[1]="X"
  print(f"{row1}\n{row2}\n{row3}")
elif position=="32":
  row2[2]="X"
  print(f"{row1}\n{row2}\n{row3}")
elif position=="13":
  row3[0]="X"
  print(f"{row1}\n{row2}\n{row3}")
elif position=="23":
  row3[1]="X"
  print(f"{row1}\n{row2}\n{row3}")
elif position=="33":
  row3[2]="X"
  print(f"{row1}\n{row2}\n{row3}")
else:
    print("Enter a valid coordinate.")