ninjas = ["Hori", "Miyamura", "Ishikawa", "Sakura"]

# for ninja in ninjas:
#     print(ninja)

# for ninja in ninjas[1:3]:  # section of list
#     print(ninja)

# for ninja in ninjas:
#     if ninja == "Miyamura":
#         print(f"{ninja} - black hair")
#         break
#     else:
#         print(ninja)

# for n in range(5):
#     print(n)

# for n in range(3, 10):  # from 3 to 9
#     print(n)

# for n in range(0, 20, 4):  # from 0 to 19 with step of 4
#     print(n)

colors = ["Pink", "Purple", "Blue", "White"]

# for i in range(len(colors)):
#     print(i, colors[i])

for i in range(
    len(colors) - 1, -1, -1
):  # the second arg (-1) meant to the -1 pos but not including so it should stop at 0
    print(i, colors[i])
