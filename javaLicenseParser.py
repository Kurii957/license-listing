from bs4 import BeautifulSoup
import os
html_input = os.path.abspath("files/dependency-management.html")
with open(html_input) as fp:
    soup = BeautifulSoup(fp, 'html.parser')

class JavaLicenseParser:

    def get_license_type(self, no_duplicates):
        td_values = []
        # a_values = []
        all_values = []
        sep = ","
        license_type_for_td = {}

        # Finding all td values in table
        for tr in soup.table:
            for td in tr:
                if td != "\n":
                    td_values.append(td.string)
                    try:
                        td_values.append(td.a.get('href'))
                    except:
                        m = 1

        # Separating specific td values
        for i in range(6, len(td_values) - 8, 8):
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

        # Matching keys from both dictionaries
        for key in license_type_for_td.keys():
            if no_duplicates.get(key):
                all_values.append(key + sep + license_type_for_td[key])

        return all_values

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


