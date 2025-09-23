import time

print("-------Create new account--------")
user = input("| User: ")
passw = input("| Password: ")
print("-------Succesfully created!------\n")
time.sleep(1)
while(True):
    ans = input("| Login now?(yes/no)\n" + "| Answer: ")
    login = ans.lower()
    if login == "yes":
        print("| Nice!\n")
        time.sleep(1)
        print("---Enter Username and password---")
        email = input("| Enter Username: ")
        password = input("| Enter password: ")
        time.sleep(1)
        print("")
        if email == user and password == passw:
            print("----------Welcome " + user +"!---------")
            break
        else:
            print("--------Wrong email or password!--------\n")
            time.sleep(1)
            continue
    elif login == "no":
        print("-----You have no choice boy!-----\n")
        time.sleep(1)
        print("---Enter Username and password---")
        email = input("| Enter Username: ")
        password = input("| Enter password: ")
        time.sleep(1)
        print("")
        if email == user and password == passw:
            print("----------Welcome " + user +"!---------")
            break