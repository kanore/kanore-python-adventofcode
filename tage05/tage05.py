import entryTage05 as e

import splitter as s

import fillStack as fs

import movingStack as ms

import gettingFinalsLetters as gfl

# split the two parts of the input
chart, moves = s.intoTwoParts(e.entry)
# split the chart by lines
chartLines = s.byLines(chart)
# fill stacks of letters for part 1
stacks1 = fs.fillStack(chartLines)
# reverse order to fill the stack later
chartLines.reverse()
# fill stacks of letters for part 2
stacks2 = fs.fillStack(chartLines)
# separate lines of moves
movesLines = s.byLines(moves)

# moving boxes 9000
result9000 = ms.movingStackBoxes9000(movesLines, stacks1)
result1 = gfl.gettingFinalsLetters(result9000)
print("Day 05 part 1 result: ", result1)

# moving boxes 9001
result9001 = ms.movingStackBoxes9001(movesLines, stacks2)
result2 = gfl.gettingFinalsLetters(result9001)
print("Day 05 part 2 result: ", result2)