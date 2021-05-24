import sys

from javaPackageParser import JavaPackageParser

if __name__ == '__main__':
    if len(sys.argv) == 4:
        input_package_file = sys.argv[1]
        input_license_file = sys.argv[2]
        output_file = sys.argv[3]
        print("Running for package input file: ", input_package_file, " licenses report", input_license_file, " and output file: ", output_file)
    else:
        print("Missing packagesinput file")
        print("Missing license file")
        print("Missing output file")
        exit(1)

    pp = JavaPackageParser(input_package_file, input_license_file, output_file)
    pp.run()