import csv
import os
import string
import sys

__author__ = "@musemby"


def anagram():
    file = sys.argv[1]
    with open(file, 'r') as f:
        reader = csv.reader(f)
        for product in reader:
            # i heard you liked strips, so I chained one to another then another
            out = [s.strip().strip('\"').strip('\'').replace(' ', '').lower() for s in product]

            first, second = out
            if sorted(first) == sorted(second):
                print('Valid Pattern')
            else:
                print('Invalid Pattern')

if __name__ ==  '__main__':
    anagram()