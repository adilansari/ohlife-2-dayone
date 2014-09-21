import argparse
from pprint import PrettyPrinter

def migrate(filename, dry_run=False):
    for line in filename:
        print line


def logger(date, content):
    pp = PrettyPrinter(indent=4)
    print str(date) + '\n' + content


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
