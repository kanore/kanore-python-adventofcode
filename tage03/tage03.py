
import entryTage03 as e

import splitRucksack as sr

import findExtraLetter as fel

import calculatePriority as cp

rucksack = sr.splitRucksack(e.entry)
print(rucksack)

allLetters = fel.findExtra(rucksack)
print(allLetters)

result1 = cp.calcPrior(allLetters)
print(result1)