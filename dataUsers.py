
def is_integer(n):
    try:
        return int(n)
    except ValueError:
        return "invalid"

class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

users = [User("andy", 17), User("juan", 16)]


# Running

while True:
    
    print("############# USER GESTION ############")
    print("::options::")
    print("show: to show all the users")
    print("new: to create a new user")
    print("del: to delet an user")
    print("exit: to exit the program")
    ans = input()

    if ans == "show":
        
        print("#--USERS--#")
        for i in range(len(users)):
            print(i, users[i].name, users[i].age)

        print("Users lenght:", len(users))
        input()

    elif ans == "new":

        print("Add a new user:")
        name = input("What is the name? ")
        age = input("What is the age? " )

        if is_integer(age) == "invalid":
            print('"' + age + '"', "is not a valid number")
            input()
        else:
            newUser = User(name, age)
            users.append(newUser)

    elif ans == "del":
        print("Select the user that you want to delete")

        for i in range(len(users)):
            print(i , users[i].name, users[i].age)

        delNum = input("Write the number ")
        delUser = is_integer(delNum)

        if is_integer(delNum) == "invalid":
            print('"' + delNum + '"', "is not a valid number")
            input()
            continue
        elif delUser >= len(users) or delUser <= -len(users):
            print("the user", delUser, "not exist!!")
            input()
            continue
        else:
            print("you selected the user:", delUser, users[delUser].name, users[delUser].age)
            desition = input("you want to delete? [Y/n] ")

            if desition == "y" or desition == "yes" or desition == "" or desition == "YES" or desition == "yes":
                users.pop(delUser)
            elif desition == "n" or desition == "no" or desition == "NO"or desition == "N":
                continue
            else:
                print("invalid input")

    elif ans == "exit":

        print("Closing..")
        break

    else:
        input("Invalid Input..")
