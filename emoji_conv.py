def emoji_convertor(message):
    words = message.split(" ")
    emojis = {":)": "😄", ":(": "🙁", "xD": "😆", "<3": "❤"}
    output = ""
    for word in words:
        output += " " + emojis.get(word, word)
    return output


message = input(">")
print(emoji_convertor(message))
