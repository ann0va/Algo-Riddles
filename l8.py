
def getCatsWithHat(numCats: int, rounds: int) -> list:
    catsArr = [False] * numCats
    for step in range(1, rounds+1):
        for catInd in range(step, numCats+1, step):
            catsArr[catInd-1] = not catsArr[catInd-1]
    return [ind+1 for ind, hasHat in enumerate(catsArr) if hasHat]
 
 
# print(getCatsWithHat(100, 100))
print(getCatsWithHat(100, 100))


