
import priorities as p

def calcPrior(entry):
    val = 0
    for x in entry:
        val += p.prior[x]
    return val