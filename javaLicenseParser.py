from bs4 import BeautifulSoup
from javaCopyrightsParser import JavaCopyrightsParser

class JavaLicenseParser:

    SEPARATOR = ','

    def __init__(self, input_license_file):
        try:
            with open(input_license_file) as fp:
                self.soup = BeautifulSoup(fp, 'html.parser')
                self.read_licenses()
        except FileNotFoundError:
            print("Can't open a licenses report file: ", input_license_file)

        self.copyrightsParser = None

    def get_license_type(self, package_name_prefix, package_name, package_version):
        return self.licenses_list.get(package_name + JavaLicenseParser.SEPARATOR + package_version + JavaLicenseParser.SEPARATOR + package_name_prefix, '-,-,-,-')

    def get_copyrights(self, package_name_prefix, package_name, package_version):
        return self.copyrights_list.get(package_name + JavaLicenseParser.SEPARATOR + package_version + JavaLicenseParser.SEPARATOR + package_name_prefix, 'No copyrights')

    def read_licenses(self):
        all_values = []
        sep = ","
        license_type_for_td = {}
        copyrights_for_license = {}

        # Finding all td values in table
        for tr in self.soup.table:
            td_values = []
            td_href = ['','']
            m = 0
            for td in tr:
                if td != "\n":
                    td_values.append(td.string)
                    try:
                        td_href[m] = td.a.get('href')
                        m = m + 1
                    except:
                        a = 1

            if len(td_values) == 0:
                continue
            package_prefix = str(td_values[0])
            package_name = str(td_values[1])
            package_version = str(td_values[2])
            license_type = str(td_values[5])
            package_url = str('https://mvnrepository.com/artifact/'  + package_prefix + '/' + package_name + '/' + package_version)

            license_url = str(td_href[1])

            # Removing commas from license types
            license_type_split = license_type.split(",")
            join_string = ""
            try:
                license_type = join_string.join(license_type_split)
            except:
                license_type = license_type

            # Getting declared licenses
            declared_license = self.get_declared_license(license_type)
            license_type += sep+declared_license

            # Getting copyrights
            self.copyrightsParser = JavaCopyrightsParser()

            not_required_licenses = {"Apache-2.0", "Public Domain", "EPL-1.0", "EPL-2.0", "MPL-2.0", "CDDL-1.0", "CDDL-1.1", "None"}

            try:
                copyright = self.copyrightsParser.read_copyrigths(license_url)
            except:
                copyright = "HTTP Error 403: Forbidden"

            all_parameters = package_name + sep + package_version + sep + package_prefix
            p = license_type + sep + package_url + sep + license_url
            license_type_for_td.setdefault(all_parameters, p)
            self.licenses_list = license_type_for_td

            copyrights_for_license.setdefault(all_parameters, copyright)
            self.copyrights_list = copyrights_for_license


    def get_declared_license(self, license_type):

        # The dictionary of the possible license types
        declared_licenses = {}
        declared_licenses["Apache-2.0"] = ("Apache", "ASL", "Apache Software Licenses", "The Apache")
        declared_licenses["MIT"] = ("MIT", "The MIT")
        declared_licenses["BSD-2-Clause"] = ("BSD-2-Clause", "BSD 2-Clause")
        declared_licenses["BSD-3-Clause"] = ("BSD-3-Clause", "BSD 3-Clause", "BSD License 3")
        declared_licenses["BSD-Equivalent"] = ("BSD-Equivalent", "BSD", "BSD License")
        declared_licenses["ISC"] = ("ISC", "ISC")
        declared_licenses["EPL-1.0"] = ("EPL-1.0", "EPL 1.0", "Eclipse Public License")
        declared_licenses["EPL-2.0"] = ("EPL-2.0", "EPL 2.0", "Eclipse Public License")
        declared_licenses["EDL-1.0"] = ("EDL-1.0", "EDL 1.0", "Eclipse Distribution")
        declared_licenses["MPL-2.0"] = ("MPL-2.0", "MPL 2.0")
        declared_licenses["CDDL-1.0"] = ("CDDL-1.0", "CDDL 1.0", "CDDL")
        declared_licenses["CDDL-1.1"] = ("CDDL-1.1", "CDDL 1.1")
        declared_licenses["CC0-1.0"] = ("CC0-1.0", "CC0 1.0")
        declared_licenses["Public Domain"] = ("Public Domain", "Public Domain")
        declared_licenses["-"] = ("None", "None")

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


