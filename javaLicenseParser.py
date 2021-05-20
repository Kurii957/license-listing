from bs4 import BeautifulSoup
with open("files/dependency-management.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

class JavaLicenseParser:

    def get_license_type(self, no_duplicates):
        td_values = []
        all_values = []
        sep = ","
        license_type_for_td = {}
        for tr in soup.table:
            for td in tr:
                if td != "\n":
                    td_values.append(td.string)

        for i in range(0, len(td_values) - 6, 6):
            package_name = str(td_values[i + 1])
            package_version = str(td_values[i + 2])
            package_prefix = str(td_values[i])
            license_type = str(td_values[i + 5])
            license_type_split = license_type.split(",")
            join_string = ""
            try:
                license_type = join_string.join(license_type_split)
            except:
                license_type = license_type

            all_parameters = package_name + sep + package_version + sep + package_prefix

            license_type_for_td.setdefault(all_parameters, license_type)

        for key in license_type_for_td.keys():
            if no_duplicates.get(key):
                all_values.append(key+sep+license_type_for_td[key])


        return all_values