import os
import re

for paths, dirs, files in os.walk("."):
    for filename in files:
        if re.search("\.c$", filename) is not None:
            path = os.path.join(paths, filename)
            line = open(path, 'r').read().split('\n')
            print(path)
            for i, row in enumerate(line):
                if re.search("[&|<>/*+=-]$", row) is not None:
                    if re.search("\*/$|\*\*$|/\*$|h>$|\\*$", row) is None:
                        print("\toperteur :",row[len(row) -1], " in  line :", i + 1, "\n")
