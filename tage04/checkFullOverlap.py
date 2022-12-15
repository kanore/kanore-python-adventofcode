def checkFullOverlap(entry):
    contains = 0

    for pairs in entry:
        elf1, elf2 = pairs.rsplit(",")
        elf1Start, elf1End = elf1.rsplit("-")
        elf2Start, elf2End = elf2.rsplit("-")

        if int(elf1Start) >= int(elf2Start) and int(elf1End) <= int(elf2End):
            contains += 1
        elif int(elf2Start) >= int(elf1Start) and int(elf2End) <= int(elf1End):
            contains += 1

    return contains