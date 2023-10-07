ninjas = ["Hori", "Miyamura", "Ishikawa", "Sakura"]

# for ninja in ninjas:
#     print(ninja)

# for ninja in ninjas[1:3]:  # section of list
#     print(ninja)

for ninja in ninjas:
    if ninja == "Miyamura":
        print(f"{ninja} - black hair")
        break
    else:
        print(ninja)

# for n in range(5):
#     print(n)

# for n in range(3, 10):  # from 3 to 9
#     print(n)

for n in range(0, 20, 4):  # from 0 to 20 with step of 4
    print(n)
