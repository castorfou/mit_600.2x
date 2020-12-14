import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    # TO DO
    new_rabbit = 0
    probability_repro = 1.0 - CURRENTRABBITPOP/MAXRABBITPOP
    
    for rabbit in range(CURRENTRABBITPOP):
        if random.random() < probability_repro:
            new_rabbit += 1
    CURRENTRABBITPOP += new_rabbit
    if (CURRENTRABBITPOP>MAXRABBITPOP):
        CURRENTRABBITPOP = MAXRABBITPOP
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    # TO DO
    delta_fox = 0
    
    for fox in range(CURRENTFOXPOP):
        can_eat_rabbit=False
        if (CURRENTRABBITPOP>10): can_eat_rabbit = True
        probability_fox_eats_rabbit=CURRENTRABBITPOP/MAXRABBITPOP
        if (can_eat_rabbit & (random.random() < probability_fox_eats_rabbit)):
            CURRENTRABBITPOP -=1
            if (random.random() < 1/3):
                delta_fox+=1
        else:
            if (random.random() < 0.9):
                if (CURRENTFOXPOP>10):  delta_fox-=1
    CURRENTFOXPOP+=delta_fox
#    if (CURRENTFOXPOP < 10): CURRENTFOXPOP=10
    
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    # TO DO
    rabbit_populations = []
    fox_populations = []
    for i in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)
    return (rabbit_populations, fox_populations)


#CURRENTRABBITPOP = 1000
#CURRENTFOXPOP = 50
#foxGrowth()
#print(CURRENTFOXPOP)
#foxGrowth()
#print(CURRENTFOXPOP)

#MAXRABBITPOP = 1000
#CURRENTRABBITPOP = 500
#rabbitGrowth()
#print(CURRENTRABBITPOP)
#rabbitGrowth()
#print(CURRENTRABBITPOP)



#results = runSimulation(20)
#print(results)
    

#CURRENTRABBITPOP = 10
#CURRENTFOXPOP = 20
#MAXRABBITPOP = 100
#print(runSimulation(100))

#CURRENTRABBITPOP = 1
#MAXRABBITPOP = 1000
#CURRENTFOXPOP = 1
#for trial in range(20):
#    foxGrowth()
#    print(CURRENTFOXPOP)

MAXRABBITPOP = 1000
CURRENTRABBITPOP = 50
CURRENTFOXPOP = 300
numSteps = 200

rabbit_populations, fox_populations = runSimulation(numSteps)

import pylab
pylab.plot(rabbit_populations, label='rabbit')
pylab.plot(fox_populations, label='fox')
pylab.xlabel('numSteps')
pylab.ylabel('population')
pylab.title('Evolution populations of rabbits and fox')
pylab.legend(loc = 'best')
pylab.show()


coeff_rabbit = pylab.polyfit(range(len(rabbit_populations)), rabbit_populations, 2)
coeff_fox = pylab.polyfit(range(len(fox_populations)), fox_populations, 2)
print(coeff_rabbit, coeff_fox)
pylab.plot(pylab.polyval(coeff_rabbit, range(len(rabbit_populations))), label='estimated rabbit')
pylab.plot(pylab.polyval(coeff_fox, range(len(fox_populations))), label='estimated fox')
pylab.xlabel('numSteps')
pylab.ylabel('population')
pylab.title('Evolution estimated population of rabbits and fox')
pylab.legend(loc = 'best')
pylab.show()

