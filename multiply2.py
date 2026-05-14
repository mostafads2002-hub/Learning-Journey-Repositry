def multiply(numbrs):
    for i in range(1 ,11):
        print(f"{numbrs}x{i}={numbrs*i}")
mm=int(input("enter a numbrs "))
print(f"multiplication table for {mm}:")
multiply(mm)
agen=input("do you want try agen?(yes,no)")
while agen=="yes":
    multiply(mm)
    agen=input("do you want try agen?(yes,no)")
print("goodbay")