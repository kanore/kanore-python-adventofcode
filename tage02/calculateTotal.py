def calculateTotal(entry):
    total = 0
    rock = 1
    paper = 2
    scissors = 3
    win = 6
    tie = 3
    lose = 0
    for x in entry:
        print(x)
        if x == 'A X': #Rock Rock
            print(x)
            total += rock + tie
            continue
        if x == 'A Y': #Rock Paper
            print(x)
            total += paper + win
            continue
        if x == 'A Z': #Rock Scissors
            print(x)
            total += scissors + lose
            continue

        if x == 'B X': #Paper Rock
            print(x)
            total += rock + lose
            continue
        if x == 'B Y': #Paper Paper
            print(x)
            total += paper + tie
            continue
        if x == 'B Z': #Paper Scissors
            print(x)
            total += scissors + win
            continue

        if x == 'C X': #Scissors Rock
            print(x)
            total += rock + win
            continue
        if x == 'C Y': #Scissors Paper
            print(x)
            total += paper + lose
            continue
        if x == 'C Z': #Scissors Scissors
            print(x)
            total += scissors + tie
            continue

    return total