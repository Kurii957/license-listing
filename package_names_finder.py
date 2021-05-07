filepath = "C:\maven\spring-petclinic\dependency_tree.txt"
tab = [] #later move data to set

try:
    file = open(filepath, "r")
    for line in file.readlines():
        tab.append(line.strip())
except FileNotFoundError:
    print("Can't find a file")

index = 0
for line in tab:
    tab[index] = tab[index].lstrip("[INFO]")
    tab[index] = tab[index].strip()
    tab[index] = tab[index].strip( )

    print(tab[index])
    index+=1
print("HEJA")
file.close()