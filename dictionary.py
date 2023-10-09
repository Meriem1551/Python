# ninja_belt = {"Crystal": "red", "ryu": "yellow"}
# # print(ninja_belt["Crystal"])

# # print("yoshi" in ninja_belt)
# # print("ryu" in ninja_belt)

# # print(ninja_belt.keys())
# # print(list(ninja_belt))
# # print(ninja_belt.values())

# vals = list(ninja_belt.values())
# # print(vals.count("red"))  # return number of the vlue passed

# ninja_belt["mario"] = "blue"

# # print(ninja_belt)

# person = dict(name="Meriem", age=19, weight="44kg")

# print(person)


# def ninja_intro(dictionary):
#     for key, val in dictionary.items():
#         print(f"I am {key} and i am a {val} belt")


def belt_count(dictionary):
    belts = list(dictionary.values())
    for belt in belts:
        num = belts.count(belt)
        print(f"There are {num} {belt} belts")


ninja_belts = {}

while True:
    ninja_name = input("Enter a ninja name: ")
    ninja_belt = input("Enter a ninja colour: ")
    ninja_belts[ninja_name] = ninja_belt

    another = input("Add another?(y/n) ")
    if another == "y":
        continue
    else:
        break

belt_count(ninja_belts)
# ninja_intro(ninja_belts)
