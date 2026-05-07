import string
ask1=input("do you want to \n1:dectrypt amessage \n2:eyptncr a message\n")
word = string.ascii_letters * 2 +string.ascii_letters
inp_words = input("Enter the word: ")
inp_numbr=int(input("Enter the encryption number"))
message=""
if ask1=="1":
    for leetar in inp_words:
        if leetar in word:
            orgnale_position = word.index(leetar)
            new_position = orgnale_position + inp_numbr
            message += word[new_position]
        else:
            message+=leetar
    print(f"Here is the encrypted word: {message}")
elif ask1=="2":
    for leetar1 in inp_words:
        if leetar1 in word:
            orgnale_position = word.index(leetar1)
            new_position = orgnale_position -inp_numbr
            message+=word[new_position]
        else:
            message+=leetar1
    print(f"Here is the encrypted word: {message}")

