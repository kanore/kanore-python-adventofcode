def calculateTotal2(entry):
    total = 0
    rock = 1
    paper = 2
    scissors = 3
    win = 6
    draw = 3
    lose = 0
    for x in entry:
        
        if x == 'A X': #Rock Lose
            
            total += lose + scissors
            continue
        if x == 'A Y': #Rock Draw
            
            total += draw + rock
            continue
        if x == 'A Z': #Rock Win
            
            total += win + paper
            continue

        if x == 'B X': #Paper Lose
            
            total += lose + rock
            continue
        if x == 'B Y': #Paper Draw
            
            total += draw + paper
            continue
        if x == 'B Z': #Paper Win
            
            total += win + scissors
            continue

        if x == 'C X': #Scissors Lose
            
            total += lose + paper
            continue
        if x == 'C Y': #Scissors Draw
            
            total += draw + scissors
            continue
        if x == 'C Z': #Scissors Win
            
            total += win + rock
            continue

    return total