import math

filepath = "files\dependency_tree.txt"
tab = []
all_names = []
one = 1
zero = 0
sep = ","

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
        tab[index] = tab[index][one:]

    # setting the prefix
    separator = tab[index].index(":")
    packet_prefix = tab[index][zero:separator]
    separator += one
    help = tab[index][separator:]

    # setting the name
    separator = help.index(":")
    packet_name = help[zero:separator]
    separator += one
    help = help[separator:]

    # setting the file type
    separator = help.index(":")
    file_type = help[zero:separator]
    separator += one
    help = help[separator:]

    # setting the version
    try:
        separator = help.index(":")
        packet_version = help[zero:separator]
        separator = packet_version.rindex(".")
        help2 = packet_version[separator+1:]
        if help2 == "Final" or help2 == "RELEASE":
            packet_version = packet_version[zero:separator]
    except:
        packet_version = help

    # moving data to table
    all = packet_name + sep + packet_version + sep + packet_prefix
    all_names.append(all)

    index+=1

# for line in all_names:
#    print(line)

# removing duplicates
no_duplicates = {}
no_duplicates[all_names[0]] = 1

for num in range(0, len(all_names)):
    no_duplicates.setdefault(all_names[num], 1)

# saving data to csv file
to_csv = open("files\java_packages.csv", "w")

keys = []

to_csv.write("Package name"+sep+"Package version"+sep+"Package name prefix\n")
for key in no_duplicates.keys():
    keys.append(key)

keys.sort()

for key in keys:
    to_csv.write(key+"\n")

to_csv.close()
file.close()
