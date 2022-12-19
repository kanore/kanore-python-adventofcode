import entryTage07 as e

import splitter as s

import dirsController as dirs

directories = s.splitBy(e.entry, """
$ ls
""")

max = 100000
dirs.savingDirs(directories)

