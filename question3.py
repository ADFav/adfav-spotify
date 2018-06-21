def question3(amount,denominations):
    def dynamicSolution(currentSum = 0,optionsIndex = 0):
        result = 0
        for i in range(optionsIndex,len(denominations)):
            if currentSum + denominations[i] < amount:
                result += dynamicSolution(currentSum+denominations[i],i)
            elif currentSum + denominations[i] == amount:
                result += 1
        return result
    return dynamicSolution()
    
# print "4,[1,2,3] ==> 4"
# print question3(4,[1,2,3]) == 4