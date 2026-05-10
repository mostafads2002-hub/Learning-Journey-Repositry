class Profile:
    def __init__(self, name,gmail,language):
        self.name=name
        self.gmail=gmail
        self.language=language
    def display(self):
        print(f"your name is:{self.name}")
        print(f"your gmail is: {self.gmail}")
        print(f"your love language is:{self.language}")


#just see no commit
ask_name=input("enter your name:\n")#السؤال عن الاسم 
ask_gmail=input("enter your gmail:\n")#الاسؤال عن اسم الجميل 
ask_language=input("enter the name of the language you are learning:\n")#السؤال عن اللغة التي يتعلمها 
first_person=Profile(ask_name,ask_gmail,ask_language)
    
#السؤال ما اذا يريد المستخدم ان يري مدخلاته
ask11=input("Do you want to see the data you entered?(yes,no)")

if ask11.lower()=="yes":
    first_person.display()
elif ask11.lower()=="no":
    print("Thank you for your participation")
else:
    print("Please enter(yes,no)")

