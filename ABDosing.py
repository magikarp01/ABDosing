import math
import random
import matplotlib.pyplot as plt

def sampleA():
    return random.random()<.9

def sampleB():
    return random.random()<.5

def ev(survivals):
    if len(survivals) == 0:
        return 0
    return sum(survivals)/len(survivals)

def UCBVal(survivals, t, c=math.sqrt(2)):
    uncertainty = c * math.sqrt(t / len(survivals))
    return ev(survivals) + uncertainty

preSamplesList = range(1, 101)
aveSamples = []

for x in preSamplesList:
    bSamples = []
    # preSamples = 50
    preSamples = x

    for i in range(1000):
        aSurvivals = [sampleA() for m in range(preSamples)]
        bSurvivals = [sampleB() for n in range(preSamples)]

        c = math.sqrt(2)
        for t in range(100):
            UCB_a = UCBVal(aSurvivals, t)
            UCB_b = UCBVal(bSurvivals, t)
            if UCB_a > UCB_b:
                aSurvivals.append(sampleA())
            else:
                bSurvivals.append(sampleB())

        # print(aSurvivals)
        # print(bSurvivals)
        # print(f"Number of A survivals is {len(aSurvivals)}, Number of B survivals is {len(bSurvivals)}")
        bSamples.append(len(bSurvivals)-preSamples)

    print(f"Average number of bSamples is {sum(bSamples)/len(bSamples)}")
    aveSamples.append(sum(bSamples)/len(bSamples))

plt.scatter(preSamplesList, aveSamples)
plt.ylabel("Number of Doses to Allocate to B")
plt.xlabel("Number of Initial Samples")
plt.title("Number of B Doses vs Initial Sampling")
plt.show()
# numSamples = [instance.get_numSamples() for instance in instances]
# return policy(values, variances, numSamples, allocSize)