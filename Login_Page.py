

def register():
    name = input("Enter your Name: ")
    age = input("Enter your age: ")
    username = (name + age)

    print("Your username is created and it is " + username + ".")
    password = input("Enter your Password: ")

    users = open("users.txt", "a")
    users.write(username)
    users.write(", ")
    users.write(password)
    users.write(", ")
    users.write("\n")
    users.close()


def login():
    logged_in = False
    username = input("Enter your Username: ")
    password = input("Enter your Password: ")
    for line in open("users.txt", "r").readlines():
        login_info = line.split(", ")
        if username == login_info[0] and password == login_info[1]:
            print("Logged in sucessfully!")
            logged_in = True
            break
    if not logged_in:
        print("Wrong username or password")

            



conformation = input("Are you a registered user? Press y to register and n to login: ")
if conformation == "n":
    login()
else:
    register()
