class Membership:
    def __init__(self,first_name,last_name,id,status="active"):
        self.first_name=first_name
        self.last_name=last_name
        self.id=id
        self.status=status
    def display(self):
        print(f"first name:{self.first_name}")
        print(f"last name:{self.last_name}")
        print(f"membership id:{self.id}")
        print(f"membership status:{self.status}")
def ask():
    first_name=input("enter your first name:")
    last_name=input("enter your last name:")
    name_id=input("enter membership id:")
    ask_status=input("enter membership status, or click enter:")
    if not ask_status:
        ask_status='inactive'
    return first_name,last_name,name_id,ask_status 



def ask_action():
    print("welcome to gym membership management\n")
    print("choose an actino:\n1.add new menber\n2.desplay all menbers\n3.search for a member\n4.exit")
    action=input("enter your choice:")
    return action
def search_by():
    


all_users=[]
choice=""
by_choice=""
while choice !="4":
    choice=ask_action()

    if choice == "1":
        data = ask()
        new_opp = Membership(*data)
        all_users.append(new_opp)
        print("member added successrully!")
    elif choice=="2":
        if not all_users:
            print("No member found!")
        else:
            for user in all_users:
                user.display()
    elif choice == "3":
       
        by_choice = search_by()
    
        if by_choice == "1": # البحث عن طريق ID
            te = input("enter the membership id to search: ")
            found = False
            for user in all_users:
                if user.id == te: # نقارن الـ id الخاص بالعضو بما أدخله المستخدم
                    user.display()
                    found = True
                    break # وجدنا العضو، نخرج من اللوب
            if not found:
                print("Member not found!")

        elif by_choice == "2": # البحث عن طريق الاسم الأول
            te = input("enter the first name to search: ")
            found = False
            for user in all_users:
                if user.first_name.lower() == te.lower(): # استخدم lower لتجنب حساسية الحروف
                    user.display()
                    found = True
            if not found:
                print("No member with this name!")

        elif by_choice == "3": # البحث عن طريق الحالة (Status)
            te = input("enter status (active/inactive): ")
            found = False
            for user in all_users:
                if user.status.lower() == te.lower():
                    user.display()
                    found = True
            if not found:
                print("No members found with this status!")
print("Exait.........")                       

