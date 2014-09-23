#!/usr/bin/python
from __future__ import print_function
import sys
import logging
import argparse

# FIXME: This is a lame way of doing this. This is what tempate engines where built for!

def main(args):
    parser = argparse.ArgumentParser(description='Generate table of name badges')
    parser.add_argument("pages", help="Number of pages in badges.pdf", type=int)

    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO)
    pages = int(args.pages)

    if pages % 2 != 0:
        logging.error('Number of pages must be even')
        sys.exit(1)

    rows = 5
    logging.info("Assume {pages} pages and {rows} rows".format(pages=pages, rows=rows))

    # We are dividing up the page into two columns
    theRange = list(range(pages//2))
    for i in theRange:
        if i % rows == 0:
            print(r"\begin{tabular}{cc}")
        print(r"\includegraphics[height=50mm,page="+str(2*i + 1) +
              r"]{badges.pdf}&\includegraphics[height=54mm,page="+ str(2*i+2) + "]{badges.pdf}"
              + (r"\\" if i%rows != (rows - 1) else '')
             )
        if i % rows == (rows - 1) or i == theRange[-1]:
            print("\\end{tabular}")

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

