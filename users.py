# ,e,e,,e
def add_user(users):
    name = input("Enter a name: ")
    try:
        ag = int(input("Enter an age: "))
    
        print("Enter a number!")
        dic = {}
        dic["name"] = name
        dic["age"] = ag
        users.append(dic)
    except ValueError:
        print("number")
    
def show_user(users):
    for i in users:
        print(i["name"], "-", i["age"])

def find_user(users):
    fus = input("Enter the name of user you want to find: ")
    c = True
    for i in users:
        if i["name"] == fus:
            print(i["name"], "-", i["age"])
            c = False
    if c:
        print("There is no such user")
    
def delete_user(users):
        dus = input("Enter the name of the user you want to delete: ")
        for i in users:
             if dus == i["name"]:
                users.remove(i)
                print("User was deleted")

def statistics(users):
    if len(users) != 0:
                print("Total users:", len(users))
            
                ad = 0
                mi = 0
                avac = 0
                eld = 0
           
                for i in users:
                    if i["age"] >= 18:
                        ad += 1
                    else:
                        mi += 1
                
                    avac = i["age"] + avac
                
                    if i["age"] >= eld:
                        eld = i["age"]
                        old = i
        
                print("Adults:", ad)
                print("Minors:", mi)
                print("Average age:", avac / len(users))
                print("Oldest:", old["name"], "-", old["age"])
            
    else:
         print("Database is empty")