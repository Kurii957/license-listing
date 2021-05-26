import os
from javaLicenseParser import JavaLicenseParser

class JavaPackageParser:

    def __init__(self, input_packages_file, input_licenses_file, output_file):
        self.input_packages = os.path.abspath(input_packages_file)
        self.input_licenses = os.path.abspath(input_licenses_file)
        self.output = os.path.abspath(output_file)
        self.licenseParser = None
        print("Running scanner on: \n", self.input_packages, "\n", self.input_licenses, "\n", self.output)

    def run(self):
        self.licenseParser = JavaLicenseParser(self.input_licenses)

        all_names = []
        sep = ","

        # checking if file exists
        tab = self.open_file()

        # deleting unnecessary signs
        for index in range(8, len(tab)-6):
            tab[index] = tab[index].lstrip("[INFO]")
            while tab[index].startswith("|") or tab[index].startswith(" ") or tab[index].startswith("+") or tab[
                index].startswith("-") or tab[index].startswith("\\"):
                tab[index] = tab[index][1:]

            s = ":"

            # setting the prefix
            packet_prefix, separator = self.separate_string(s, tab[index])
            help = tab[index][separator:]

            # setting the name
            packet_name, separator = self.separate_string(s, help)
            help = help[separator:]

            # setting the file type
            file_type, separator = self.separate_string(s, help)
            help = help[separator:]

            # setting the version
            packet_version = self.get_version(s, help)

            # getting the license
            package_license = self.licenseParser.get_license_type(packet_prefix, packet_name, packet_version)

            # getting the copyrights
            copyrights = self.licenseParser.get_copyrights(packet_prefix, packet_name, packet_version)

            # moving data to table
            all = packet_name + sep + packet_version + sep + packet_prefix + sep + package_license + sep + copyrights
            all_names.append(all)

            index += 1

        # removing duplicates
        no_duplicates = {}
        no_duplicates[all_names[0]] = 1

        self.remove_duplicates(all_names, no_duplicates)

        # saving data to csv file
        self.write_to_file(no_duplicates, sep)

    def write_to_file(self, no_duplicates, sep):
        try:
            to_csv = open(self.output, "w")
            keys = []
            to_csv.write("Package name" + sep + "Package version" + sep + "Package name prefix" + sep + "License type" + sep + "Declared License" + sep + "Package URL" + sep + "License URL" + sep + "Copyrights\n")

            for key in no_duplicates.keys():
                keys.append(key)
            keys = sorted(keys, key=str.lower)
            for key in keys:
                to_csv.write(key + "\n")
            to_csv.close()
        except FileNotFoundError:
            print("Can't write to a file: ", self.output)

    def remove_duplicates(self, all_names, no_duplicates):
        for num in range(0, len(all_names)):
            no_duplicates.setdefault(all_names[num], 1)

    def open_file(self):
        tab = []
        try:
            in_file = open(self.input_packages, "r")
            for line in in_file.readlines():
                tab.append(line.strip())  # moving values to table
            in_file.close()
        except FileNotFoundError:
            print("Can't open a file: ", self.input_packages)
        return tab

    def separate_string(self, s, help):
        separator = help.index(s)
        separated_part = help[0:separator]
        separator += 1
        return separated_part, separator

    def get_version(self, s, raw_version):
        try:
            separator = raw_version.index(s)
            packet_version = raw_version[0:separator]
        except:
            packet_version = raw_version
        return packet_version