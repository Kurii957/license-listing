import sys

from packageParser import JavaPackageParser

if __name__ == '__main__':
    if len(sys.argv) == 3:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        print("Running for input file: ", input_file, " and output file: ", output_file)
    else:
        print("Missing input file")
        print("Missing output file")
        exit(1)

    pp = JavaPackageParser(input_file, output_file)
    pp.run()