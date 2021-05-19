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
            td = str(td).lstrip("<th>")
            td = str(td).lstrip("<td>")
            td = str(td).rstrip("</th>")
            td = str(td).rstrip("</td>")
            td_values.append(td)

for i in range(0, len(td_values)-6, 6):
    package_name = str(td_values[i+1])
    package_version = str(td_values[i+2])
    package_prefix = str(td_values[i])
    license_type = str(td_values[i+5])

    all_parameters = package_name+separator+package_version+separator+package_prefix+separator+license_type

    all_values.append(all_parameters)

for val in all_values:
    print(val)
    print()

"""  
import xml.etree.ElementTree as ET
tree = ET.parse('files/dependency-management.html')
root = tree.getroot()

for dependencies in root:
    for dependency in dependencies.findall('dependency'):
        groupId = dependency.find('groupId')
        artifactId = dependency.find('artifactId')
        version = dependency.find('version')
        list = dependency.find('licenses')


        prefix_name = groupId.text
        package_name = artifactId.text
        package_version = version.text
        print(package_name+","+package_version+","+prefix_name)
"""




"""
for dependencies in root:
    print(dependencies.tag, dependencies.attrib)
    for dependency in dependencies:
        print('|-->', dependency.tag, dependency.attrib)
        for name in dependency:
            print('|     |-->', name.tag, name.attrib)
            for license in name:
                print('|          |-->', license.tag, license.attrib)
                for thing in license:
                    print('|               |-->', thing.tag, thing.attrib)
                    for word in thing:
                        print('|               |-->', word.tag, word.txt)
"""


