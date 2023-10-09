my_name = "ryu"


def print_name():
    global my_name  # forcing the use of yoshi as a global var
    my_name = "Yoshi"
    print("The name inside the function is: ", my_name)


print_name()
print("The name outside the function is: ", my_name)
