def greet(
    name="ryu", time="night"
):  # this should work even if we dont pass params inthe call func; it's called default param
    print(f"Good {time} {name}, hope you are well")


# name = input("Enter your name: ")
# time = input("Enter the time of day: ")

greet()  # if we pass param here it will overwrite the default one

# adding default params
