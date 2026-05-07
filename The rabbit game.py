print("welcome to place the rabbit\n")
field=[['🌿','🌿','🌿'],['🌿','🌿','🌿'],['🌿','🌿','🌿']]
print(f"{field[0]}\n{field[1]}\n{field[2]}")
print("\nwhere should the rabbit go?🐇")
positeon=(input("please choose a row and a column"))
row=int(positeon[0])
column=int(positeon[1])
field[row-1][column-1]="🐇"
print("\nsyccess....\n")
print(f"{field[0]}\n{field[1]}\n{field[2]}")
