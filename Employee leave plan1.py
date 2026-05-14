import time
import os
class Emplohee():
    def __init__(self,name,date_departure,return_date):
        self.name=name
        self.date_departure=date_departure
        self.return_date=return_date

    def changing(self,name,date_departure,return_date):
        self.name=name
        self.date_departure=date_departure
        self.return_date=return_date
    def printf(self):
        print(f"{self.name}:Your vacation starts from the ({self.date_departure}-------->{self.return_date})")
def asks():
    print("\nWelcom,plwase introduce yourself......\n")
    first_ask=int(input("""1:im a manager and i'want to add or remove or change something in the vacation list
2:you are an amployee and want to know when your vacation is
3:print the vacation list.
4:exit the program
your choice------>"""))

    return first_ask
def clear():
    print("****the screen will be cleared**** ")
    time.sleep(7)
    os.system('cls' if os.name == 'nt' else 'clear')    
all_amployee=[]
choice=asks()
while choice !=4:
    if choice==1:
        pass_mang=int(input("enter a password: "))
        if pass_mang!=246810:
            print("the password is incorrect.")
            clear()
            choice=asks()
        else:
            k=int(input("Do you want to \n1:add \n2:remove\n3:change\nyour choice------> "))
            if k ==1:    
                s1=input("enter the employee's full name:")
                s2=input("enter the departure date:")
                s3=input("enter the return date:")
                new=Emplohee(s1,s2,s3)
                all_amployee.append(new)
                print("\nThe addition was successful........\n")
                clear()
                choice=asks()
            elif k ==2:
                if not all_amployee:
                    print("You have not added any employees to the leave list yet..!!!!!")
                    clear()
                    choice=asks()
                else:
                    remove_employee=input("enter the name of the employee whose seave you want to remove: ")
                    found=False
                    for i in all_amployee:
                        if i.name == remove_employee.lower():
                            all_amployee.remove(i)
                            print("the deletion was successful.......")
                            found=True
                            break
                        elif not found:
                            print("there is no employee with that name")
                    clear()
                    choice=asks()
            elif k==3:
                if not all_amployee :
                    print("You have not added any employees to the leave list yet..!!!!!")
                    clear()
                    choice=asks()
                else:
                    for i in all_amployee :
                        s4=input("Write the name of the employee whose leave you want to change.")
                        if i.name==s4:
                            i.printf()
                            s1=input("enter the employee's full name:")
                            s2=input("enter the departure date:")
                            s3=input("enter the return date:")
                            i.changing(s1,s2,s3)
                            print("\nThe change was successful......\n")
                    clear()
                    choice=asks()
    elif choice==2:
        if not all_amployee:
            print("no details were entered into the vacation list.")
            clear()
            choice=asks()
        else:
            ask_amployee=input("enter the your full name: ")
            for l in all_amployee:
                if l.name==ask_amployee:
                    l.printf()
                else:
                    print("your name is not on the leave list please contact your mananger.")
            clear()
            choice=asks()
    elif choice==3:
        if not all_amployee:
            print("You have not added any employees to the leave list yet..!!!!!")
        else:
            for i in all_amployee:
                i.printf()
            clear()
            choice()
input("the necessary action has been taken. clickto exit........")