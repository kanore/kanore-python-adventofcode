import entryTage07 as e

import splitter as s

import sumDir as sd

directories = s.splitBy(e.entry, """
$ ls
""")

max = 100000
sd.sumDir(directories, max)

