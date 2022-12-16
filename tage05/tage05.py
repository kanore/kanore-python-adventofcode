import entryTage05 as e

import splitter as s

import fillStack as fs

import movingStackBoxes as msb

import gettingFinalsLetters as gfl

# split the two parts of the input
chart, moves = s.intoTwoParts(e.entry)

# split the chart by lines
chartLines = s.byLines(chart)

# fill stacks of letters
stacks = fs.fillStack(chartLines)

# separate lines of moves
movesLines = s.byLines(moves)

# moving boxes
resultOfMoving = msb.movingStackBoxes(movesLines, stacks)

result1 = gfl.gettingFinalsLetters(resultOfMoving)
print("Day 05 part 1 result: ", result1)



# print("Day 05 part 2 result: ", result2)