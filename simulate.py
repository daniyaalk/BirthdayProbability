import pylab, random, time

i = int(input("What is the Maximum number of people you wish to test for? "))
trials = int(input("What is the number of trials for every test(More is better, but slower)? "))


def birthdayProbability(n, trials):

    successes = 0
    for trial in range(trials):

        #Reset data before each trial
        matched = False

        #print(trial,str(days))

        #Generate random dataset
        birthdays = [0]*365
        for person in range(n):
            randomday = random.randint(1,365)
            birthdays[randomday-1] += 1

        for day in range(365):
            if birthdays[day]>1:
                matched=True

        if matched==True:
            successes+=1

        #print("Trial", trial+1, "of", trials, (trial+1)*100/trials, "% | Matched: ", str(matched))
    return float(successes)*100.000000000/float(trials)

n = 0
points = []

pylab.show()


while n <= i:
    prob=birthdayProbability(n, trials)
    points.append(prob)
    pylab.scatter(n, prob, c='r')
    pylab.plot(points, c='b')
    pylab.pause(0.001)

    if(n%10==0): print("Probability for n =", n, "is", prob)

    #if(n==0): pylab.pause(10)

    n+=1

#print(birthdayProbability(23, 10000))
