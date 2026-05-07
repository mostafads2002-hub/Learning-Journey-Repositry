class Profel:
    def __init__(self,first_name,last_name,email,password,status='inactive'):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.password=password
        self.status=status

    def display(self):
        print("Displaying all users....")
        print(f"First Name:{self.first_name}")
        print(f"Last Name:{self.last_name}")
        print(f"Email:{self.email}")
        print(f"Status:{self.status}")
def ask():
    ask_first_name=input("enter your first name:")
    last_name=input("enter your last name:")
    email=input("ente r your email:")
    password=input("enter your password:")
    return password,email,last_name,ask_first_name
def ask_action():
    print("***Welcome to user management***\n")
    print("Choose an Action")
    ask_new=input("1.Add new user\n2.Displat all users\n3.Exit\nEnter your choice (1,2,3):")
    return ask_new

all_users=[]#لتخزين البيانات التي سننشئها
choice=""#متغير للتحكم في الحلقة 
while choice != "3":
    choice = ask_action()  # سطر واحد فقط يكفي لتحديث الاختيار
    
    if choice == "1":
        data = ask()
        new_opp = Profel(*data)
        all_users.append(new_opp)
        print("**********\nUser added successfully!\n**********")
        
    elif choice == "2":
        if not all_users:
            print("No users found!")
        else:
            f=int(input(f"Enter the user index there are {len(all_users)}"))
            if 0 <= f < len(all_users):
            # الوصول المباشر للقائمة باستخدام الفهرس
                all_users[f+1].printt() 
            else:
                print("Invalid index!")









