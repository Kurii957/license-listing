filepath = "C:\maven\spring-petclinic\dependency_tree.txt"
tab = []
all_names = []

# checking if file exists
try:
    file = open(filepath, "r")
    for line in file.readlines():
        tab.append(line.strip()) # moving values to table
except FileNotFoundError:
    print("Can't find a file")

index = 0
for line in tab:
    # deleting unnecessary signs
    tab[index] = tab[index].lstrip("[INFO]")
    while tab[index].startswith("|") or tab[index].startswith(" ") or tab[index].startswith("+") or tab[index].startswith("-") or tab[index].startswith("\\"):
        tab[index] = tab[index][1:]

    # setting the prefix
    separator = tab[index].index(":")
    packet_prefix = tab[index][0:separator]
    separator += 1
    help = tab[index][separator:]

    # setting the name
    separator = help.index(":")
    packet_name = help[0:separator]
    separator += 1
    help = help[separator:]

    # setting the file type
    separator = help.index(":")
    file_type = help[0:separator]
    separator += 1
    help = help[separator:]

    # setting the version
    try:
        separator = help.index(":")
        packet_version = help[0:separator]
        separator += 1
        help = help[separator:]
    except:
        packet_version = help

    # moving data to table
    all = packet_name + ";" + packet_version + ";" + packet_prefix
    all_names.append(all)

    index+=1

for line in all_names:
    print(line)

file.close()