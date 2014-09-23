#!/usr/bin/python
import argparse
import csv
import sys

def main(args):
    parser = argparse.ArgumentParser(description='Extract relevant columns from csv')
    parser.add_argument("input", help="Input CSV file", type=argparse.FileType('r'))
    parser.add_argument("output", help="Output filename", type=argparse.FileType('w'))
    parsedArgs = parser.parse_args(args)

    with parsedArgs.input as f:
        original=csv.reader(f)
        with parsedArgs.output as outf:
            result = csv.writer(outf)
            rowCounter=0
            for orow in original:
                # Last Name, First Name, Company, Ticket type
                x=orow[1:]
                print(x)
                result.writerow(x)
                rowCounter +=1

            if rowCounter % 2 != 0:
                # HACK enforce even number of rows
                print("HACK!")
                result.writerow( [ 'LastName', 'Firstname', 'Company', 'Dummy'])


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
