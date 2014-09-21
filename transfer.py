import argparse
import datetime
import os
from pprint import PrettyPrinter


def migrate(filename, dry_run=False):
    date = None
    tmp_file = 'data/tmp.txt'

    for line in filename:
        if is_date(line):
            if date:
                write_to_dayone(date, tmp_file)    # Write to dayone
                open(tmp_file, 'w').close()     # flush the temporary file
            date = strip_to_date(line)
        else:
            write_to_tmp(line, tmp_file)     # clean up the line and append to tmp.txt

    write_to_dayone(date, tmp_file)
    os.remove(tmp_file)


def write_to_dayone(date, tmp_file):
    with open(tmp_file, 'r') as content:
        print date + '\n' + content.read()


def write_to_tmp(text, tmp_file):
    text = clean_text(text)
    if text is not None:
        with open(tmp_file, 'a') as tmp_file:
            tmp_file.write(text + '\n')

def clean_text(text):
    text = text.strip('\n').strip('\r').strip(' ')
    if len(text) == 0:
        return None

    if '-' not in text[:4]:
        text = '- '+ text
    return text


def is_date(date_text):
    try:
        datetime.datetime.strptime(strip_to_date(date_text), '%Y/%m/%d')
    except ValueError:
        # raise ValueError("Incorrect data format, should be YYYY/MM/DD")
        return False

    return True
    

def strip_to_date(date_text):
    return date_text.strip('\n').strip('\r').replace('-','/')


def main():

    parser = argparse.ArgumentParser(description="""Migrate ohlife export data file to dayone app""")
    parser.add_argument('-d', '--no-dry-run', default=True,
                        dest="dry_run",
                        action="store_false",
                        help="""Actually write to mongo""")
    parser.add_argument('-f', default='data/sample.txt',
                    dest="filename",
                    type=argparse.FileType('r'),
                    help="""filename including path to load from, by default it will look for data/sample.txt""")
    
    args = parser.parse_args()
    
    migrate(args.filename, args.dry_run)


if __name__ == '__main__':
    main()
