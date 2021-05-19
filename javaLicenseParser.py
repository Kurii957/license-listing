import xml.etree.ElementTree as ET
tree = ET.parse('files/licenses.xml')
root = tree.getroot()

for dependencies in root:
    print(dependencies.tag, dependencies.attrib)
    for dependency in dependencies:
        print(' |-->', dependency.tag, dependency.attrib)
        for name in dependency:
            print(' |------>', name.tag, name.attrib)
            for license in name:
                print(' |---------->', license.tag, license.attrib)
                for thing in license:
                    print(' |-------------->', thing.tag, thing.attrib)
                    for word in thing:
                        print(' |-------------->', word.tag, word.txt)