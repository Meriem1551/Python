from random import randint

ninja_words = [
    "Aiki",
    "Buyu",
    "Chimonjutsu",
    "Cho sen",
    "Dojo",
    "Gakusei",
    "Haiboku",
    "Jin",
    "Kenshi",
    "Obake ken",
    "Rakusha",
    "Sanmaru",
    "Tekkon",
    "Yoko",
]

paragraphs = int(input("How many paragraphs of ninja ipsum: "))


def ninjarize(word):
    random_pos = randint(0, len(ninja_words) - 1)
    return f"{word} {ninja_words[random_pos]}"


with open("./files/ipsum.txt") as ipsum_original:
    items = ipsum_original.read().split()

    for n in range(paragraphs):
        ninja_text = list(map(ninjarize, items))
        with open("./files/ninja_ipsum.txt", "a") as ipsum_ninja:
            ipsum_ninja.write("".join(ninja_text) + "\n\n")
