ninja_belt = {"Crystal": "red", "ryu": "yellow"}
# print(ninja_belt["Crystal"])

# print("yoshi" in ninja_belt)
# print("ryu" in ninja_belt)

# print(ninja_belt.keys())
# print(list(ninja_belt))
# print(ninja_belt.values())

vals = list(ninja_belt.values())
# print(vals.count("red"))  # return number of the vlue passed

ninja_belt["mario"] = "blue"

# print(ninja_belt)

person = dict(name="Meriem", age=19, weight="44kg")

print(person)
