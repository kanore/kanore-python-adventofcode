
import entryTage01 as e

import findBiggest as fb

import groupByElves as g

result1 = fb.findBiggest(g.groupByElves(e.entry))

print("Day 01 part 1 result: ", result1)

import findThreeBiggest as ftb

result2 = ftb.findThreeBiggest(g.groupByElves(e.entry))

print("Day 01 part 2 result: ", result2)