ss=[]
mm=[]
print("****Welconr to ishop calcrlator****")
itmes=int(input("How many items are there in your asket today?\n"))
print("let's get to counting them....")
for l in range(0,itmes):
    ask1=input(f"Please tell me the name of the item numger {l+1}\n")
    ss.append(ask1)
    ask2=int(input(f"what is the price of {ask1}\n"))
    mm.append(ask2)
ask_to_see1=input("Do you like to see your entire basket items?\n")
if ask_to_see1.lower()=="yes":
    print(ss)
ask_to_see2=input("Would you like to see how much it'll cost?\n")
if ask_to_see2.lower()=="yes":
    print(sum(mm))