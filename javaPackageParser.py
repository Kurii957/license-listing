class JavaPackageParser:

    def __init__(self, input_file, output_file):
        self.input = input_file
        self.output = output_file

    def run(self):

        tab = []
        all_names = []
        one = 1
        zero = 0
        sep = ","

        # checking if file exists
        try:
            file = open(self.input, "r")
            for line in file.readlines():
                tab.append(line.strip())  # moving values to table
        except FileNotFoundError:
            print("Can't find a file")

        index = 0
        for line in tab:
            # deleting unnecessary signs
            tab[index] = tab[index].lstrip("[INFO]")
            while tab[index].startswith("|") or tab[index].startswith(" ") or tab[index].startswith("+") or tab[
                index].startswith("-") or tab[index].startswith("\\"):
                tab[index] = tab[index][one:]

            s = ":"

            # setting the prefix
            packet_prefix, separator = self.separate(s, tab[index], one, zero)
            help = tab[index][separator:]

            # setting the name
            packet_name, separator = self.separate(s, help, one, zero)
            help = help[separator:]

            # setting the file type
            file_type, separator = self.separate(s, help, one, zero)
            help = help[separator:]

            # setting the version
            packet_version = self.set_version(s, help, zero)

            # moving data to table
            all = packet_name + sep + packet_version + sep + packet_prefix
            all_names.append(all)

            index += 1

        # removing duplicates
        no_duplicates = {}
        no_duplicates[all_names[0]] = 1

        for num in range(0, len(all_names)):
            no_duplicates.setdefault(all_names[num], 1)

        # saving data to csv file
        to_csv = open(self.output, "w")

        keys = []

        to_csv.write("Package name" + sep + "Package version" + sep + "Package name prefix\n")
        for key in no_duplicates.keys():
            keys.append(key)

        keys.sort()

        for key in keys:
            to_csv.write(key + "\n")

        to_csv.close()
        file.close()

    def separate(self, s, help, one, zero):
        separator = help.index(s)
        separated_part = help[zero:separator]
        separator += one
        return separated_part, separator

    def set_version(self, s, help, zero):
        try:
            separator = help.index(s)
            packet_version = help[zero:separator]
            separator = packet_version.rindex(".")
            help2 = packet_version[separator + 1:]
            if help2 == "Final" or help2 == "RELEASE":
                packet_version = packet_version[zero:separator]
        except:
            packet_version = help
        return packet_version
