import entryTage05 as e

import splitter as s

import fillStack as fs

import movingStackBoxes as msb

# split the two parts of the input
chart, moves = s.intoTwoParts(e.entry)

# split the chart by lines
chartLines = s.byLines(chart)

# fill stacks of letters
stacks = fs.fillStack(chartLines)

# separate lines of moves
movesLines = s.byLines(moves)

result1 = msb.movingStackBoxes(movesLines, stacks)
print("Day 05 part 1 result: ", result1)



# print("Day 05 part 2 result: ", result2)