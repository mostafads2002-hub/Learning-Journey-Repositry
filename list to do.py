finsh=[]
no_finsh=[]
bb=input("enter your tasks for today separated by a comma:\n").split(", ")
for dd in bb:
    print(dd)
    ask=input(f"Did you finish{dd}?")
    if ask.lower()=="yes":
        finsh.append(dd)
        print("nice job")
    else:
        print("try not to put it off")
        no_finsh.append(dd)
ask2=input("Do you want to see your today's progress?(yes,no)")
if ask2=="yes":
    print(f"**********Done Tasks********\n{finsh}")
    print(f"*********Ongoing Tasks********\n {no_finsh}")






