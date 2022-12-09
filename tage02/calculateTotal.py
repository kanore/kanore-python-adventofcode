def calculateTotal(entry):
    total = 0
    rock = 1
    paper = 2
    scissors = 3
    win = 6
    draw = 3
    lose = 0
    for x in entry:
        
        if x == 'A X': #Rock Rock
            
            total += rock + draw
            continue
        if x == 'A Y': #Rock Paper
            
            total += paper + win
            continue
        if x == 'A Z': #Rock Scissors
            
            total += scissors + lose
            continue

        if x == 'B X': #Paper Rock
            
            total += rock + lose
            continue
        if x == 'B Y': #Paper Paper
            
            total += paper + draw
            continue
        if x == 'B Z': #Paper Scissors
            
            total += scissors + win
            continue

        if x == 'C X': #Scissors Rock
            
            total += rock + win
            continue
        if x == 'C Y': #Scissors Paper
            
            total += paper + lose
            continue
        if x == 'C Z': #Scissors Scissors
            
            total += scissors + draw
            continue

    return total