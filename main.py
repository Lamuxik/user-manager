from users import add_user, show_user, find_user, delete_user, statistics, count_adults
from storage import save_users, load_users

users = []
print("1. Add user\n2. Show user\n3. Find user\n4. Delete user\n5. Show statistics\n6. Count adults\n7. Save\n8. Load\n9. Exit")


while True:
    try:
        num = int(input("Enter the number of the command you want to choose: "))
    
     
        if num == 1:
            add_user(users)
        elif num == 2:
            show_user(users)
        elif num == 3:
            find_user(users)
        elif num == 4:
            delete_user(users)
        elif num == 5:
            statistics(users)
        elif num == 6:
            print(count_adults(users))
        elif num == 7:
            save_users(users)
        elif num == 8:
            users = load_users()
        elif num == 9:
            break
        else:
            print("Enter a correct nummberrr!!")
    except ValueError:
        print("NUMBER")
    
    
        
        

 