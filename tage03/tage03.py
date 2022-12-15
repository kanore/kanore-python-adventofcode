
import entryTage03 as e

import splitRucksack as sr

import findExtraLetter as fel

import calculatePriority as cp

#part 1
rucksack = sr.splitRucksack(e.entry)
allLetters = fel.findExtra(rucksack)
result1 = cp.calcPrior(allLetters)
print(result1)

import commonItems as ci

#part 2
#get commons letters between the three rucksack
items = ci.commonItems(rucksack)

#calculate prior
result2 = cp.calcPrior(items)
print(result2)