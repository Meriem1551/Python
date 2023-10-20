ipsum_file = open("files/ipsum.txt")


# for line in ipsum_file:
#     print(line.rstrip())

# ipsum_file.seek(100)#puting the cursor at pos 100

# lines = ipsum_file.readlines()
# print(lines)

# ipsum_file.seek(50)  # start from pos 50
# file_text = ipsum_file.read(100)  # return 100 chars from pos 50
# print(file_text)

# ipsum_file.close()


def sequence_filter(line):
    return ">" not in line


with open("files/dna_sequence.txt") as dna_file:
    lines = dna_file.readlines()
    print(list(filter(sequence_filter, lines)))
