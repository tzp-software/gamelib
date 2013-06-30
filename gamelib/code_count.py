'''
code_count.py

    to count lines of code in files. Dosent count empty lines, cheaters
@author: Kyle Roux
'''
import sys

code = sys.argv[1]

f = open(code,'r')

def count_lines(doc):
    count = 0
    for line in doc.readlines():
        if line.strip() != '':
            count += 1
    doc.close()
    return count

def main():
    print '{} non-empty lines of code'.format(count_lines(f))

if __name__ == "__main__":
    main()

