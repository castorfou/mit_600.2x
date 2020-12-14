import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    # TODO
    pylab.hist(values, bins=numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if (title is not None):
        pylab.title(title)
    pylab.show()
    
#xVals = []
#for i in range(1000):
#    xVals.append(random.random())
#makeHistogram(xVals, 10, 'random X', '# of value', title='Beautiful histo')    
              
#makeHistogram([1,2], 4, "Aaa", "Bbb")              

def longestRun(roll):
    """
      - roll: a dice roll (is a list)
      - returns the longest run:  counts the number of times the same dice value shows up in consecutive rolls
    """
    if (len(roll) < 2):
        return len(roll)
    longest_run = 1
    previous_roll = None
    local_longest_run = 1
    for roll_result in roll:
        if (previous_roll is None):
            previous_roll = roll_result
        else:
            if (previous_roll == roll_result):
                local_longest_run += 1
                if (local_longest_run > longest_run):
                    longest_run = local_longest_run
            else:
                local_longest_run = 1
                previous_roll = roll_result
    
    return longest_run


                    
# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    # TODO
    longestruns=[]
    mean_longestruns = 0
    for trial in range(numTrials):
        tirage=[]
        for tir in range(numRolls):
            tirage.append(die.roll())
#        print(tirage)
        run = longestRun(tirage)
        longestruns.append(run)
        mean_longestruns += run
    makeHistogram(longestruns, 10, 'longest runs', 'occurence', title='longest runs for all trials')
    
    return round(mean_longestruns/numTrials, 3)
        
#getAverage(Die([1,2,3,4,5,6]), 10, 3)
#print(longestRun(getAverage(Die([1,2,3,4,5,6]), 100, 1)))
# One test case
print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000))