
import priorities as p

def calcPrior(entry):
    print(len(entry))
    val = 0
    for x in entry:
        val += p.prior[x]
    return val