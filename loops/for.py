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
