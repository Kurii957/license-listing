from bs4 import BeautifulSoup

with open("files/dependency-management.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

td_values = []
all_values = []
all_parameters = ''
separator = ","

for tr in soup.table:
    for td in tr:
        if td != "\n":
            td_values.append(td.string)

for i in range(0, len(td_values)-6, 6):
    package_name = str(td_values[i+1])
    package_version = str(td_values[i+2])
    package_prefix = str(td_values[i])
    license_type = str(td_values[i+5])

    all_parameters = package_name+separator+package_version+separator+package_prefix


    all_values.append(all_parameters)

for val in all_values:
    print(val)
    print()



