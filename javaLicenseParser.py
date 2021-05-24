from bs4 import BeautifulSoup
import os


class JavaLicenseParser:

    SEPARATOR = ','

    def __init__(self, input_license_file):
        try:
            with open(input_license_file) as fp:
                self.soup = BeautifulSoup(fp, 'html.parser')
                self.read_licenses()
        except FileNotFoundError:
            print("Can't open a licenses report file: ", input_license_file)

    def get_license_type(self, package_name_prefix, package_name, package_version):

        # kod do napisania
        license_type = 'MIT'

        return self.licenses_list.get(package_name + JavaLicenseParser.SEPARATOR + package_name_prefix + JavaLicenseParser.SEPARATOR + package_version, '----')

    def read_licenses(self):
        td_values = []
        # a_values = []
        all_values = []
        sep = ","
        license_type_for_td = {}

        # Finding all td values in table
        for tr in self.soup.table:
            td_values = []
            for td in tr:
                if td != "\n":
                    td_values.append(td.string)
                    try:
                        td_values.append(td.a.get('href'))
                    except:
                        m = 1
            i = 0
            package_prefix = str(td_values[i])
            package_name = str(td_values[i + 1])
            package_url = str(td_values[i+2])
            package_version = str(td_values[i + 3])
            license_type = str(td_values[i + 6])
            license_url = str(td_values[i + 7])

            # Removing commas from license types
            license_type_split = license_type.split(",")
            join_string = ""
            try:
                license_type = join_string.join(license_type_split)
            except:
                license_type = license_type
            print(package_prefix, package_name, package_url, package_version, license_type, license_url)
            # Getting declared licenses
            declared_license = self.get_declared_license(license_type)
            license_type += sep+declared_license

            all_parameters = package_name + sep + package_version + sep + package_prefix
            p = license_type + sep + package_url + sep + license_url
            license_type_for_td.setdefault(all_parameters, p)
            self.licenses_list = license_type_for_td


    def get_declared_license(self, license_type):

        # The dictionary of the possible license types
        declared_licenses = {}
        declared_licenses["Apache-2.0"] = ("Apache", "ASL", "Apache Software Licenses", "The Apache")
        declared_licenses["MIT"] = ("MIT", "The MIT")
        declared_licenses["BSD-2-Clause"] = ("BSD-2-Clause", "BSD 2-Clause")
        declared_licenses["BSD-3-Clause"] = ("BSD-3-Clause", "BSD 3-Clause", "BSD License 3")
        declared_licenses["BSD-Equivalent"] = ("BSD-Equivalent", "BSD", "BSD License")
        declared_licenses["ISC"] = ("ISC", "ISC")
        declared_licenses["EPL-1.0"] = ("EPL-1.0", "Eclipse Public License")
        declared_licenses["EPL-2.0"] = ("EPL-2.0", "Eclipse Public License")
        declared_licenses["EDL-1.0"] = ("EDL-1.0", "EDL 1.0", "Eclipse Distribution")
        declared_licenses["MPL-2.0"] = ("MPL-2.0", "MPL 2.0")
        declared_licenses["CDDL-1.0"] = ("CDDL-1.0", "CDDL 1.0", "CDDL")
        declared_licenses["CDDL-1.1"] = ("CDDL-1.1", "CDDL 1.1")
        declared_licenses["CC0-1.0"] = ("CC0-1.0", "CC0 1.0")
        declared_licenses["Public Domain"] = ("Public Domain", "Public Domain")
        declared_licenses["None"] = ("None", "None")

        # not_required_license = {"Apache-2.0", "Public Domain", "EPL-1.0", "EPL-2.0", "MPL-2.0", "CDDL-1.0", "CDDL-1.1", "None"}
        declared_license = ''
        k = 0

        for key in declared_licenses.keys():
            for value in declared_licenses[key]:
                bool = license_type.startswith(value)
                if bool:
                    declared_license = key
                    k += 1
                    break
                else:
                    continue
            if k >= 1:
                break

        if declared_license == '':
            declared_license = license_type

        return declared_license


