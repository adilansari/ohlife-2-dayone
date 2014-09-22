Popular private daily blogging service [Ohlife announced](http://ohlife.com/shutdown) its shutdown today.

#### DayOne
1. [DayOne](http://dayoneapp.com) is a solution that provides a good experience for daily loggers.
2. All the data is on your local device and you can backup to your Dropbox, iCloud or any other Cloud storage
3. Less dependencies.


##### Migrating data from OhLife to DayOne
1. Unfortunately, there is no official export tool. The [OhLife export](https://ohlife.com/export) tool just gets you a single huge __*.txt__ file with all your entries.
2. I wrote this script to format and import data into DayOne app.


##### Getting DayOne and CLI
1. Install [DayOne](http://dayoneapp.com) app on Mac(_Unfortunately no Win32/Linux_) and run it.
2. Go to __> DayOne__ on top bar and click on _Install Command Line Tools_ or download from [here](https://dayone.zendesk.com/hc/en-us/articles/200258954-Day-One-Tools).
3. The command line interface is pretty straightforward, [manual](http://dayoneapp.com/tools/cli-man/).


#### Importing data to DayOne
1. Clone this repo.

2. Help options:
```
$ python transfer.py --help

usage: transfer.py [-h] [-d] [-f FILENAME]

Migrate ohlife export data file to dayone app

optional arguments:
  -h, --help        Show this help message and exit
  -d                Actually write to dayone
  -f FILENAME       Filename including path to load from, by default it will
                    look for data/sample.txt

```

**Note**: You may need to change the formatting as per content, current output is as following:
![Sample Entry in DayOne app](https://raw.github.com/adilansari/ohlife-2-dayone/master/dayone_app_sample.png)