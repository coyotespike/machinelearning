"""
We want to flip 1000 fair coins, flipping each 10 times. From these 1000 coins,
we will choose 3: the first one flipped, a random coin, and the one with the
minimum number of heads (in case of tie, the first such). We then take the 
fraction of heads obtained out of 10 tosses.

Run this 100,000 times to get a good distribution.
"""

# Flip them, return the fraction of heads
# Choose the first, a random one, and the lowest fraction of heads
# store the results in three separate lists
# take the average of v_min
# plot the results on a log-log scale to see the distribution

import random
import pylab
from matplotlib import mlab
import numpy
import matplotlib.pyplot as plt
from matplotlib import pyplot

def coinFlip(size, number_of_runs):
    # set up three lists to hold our results
    v1 = []
    v_rand = []
    v_min = []
    count = 0
    # run 100,000 times
    for run in xrange(number_of_runs):
        # set up 1000 coins
        c_min = 1
        for coin in xrange(1, size+2):
            # flip each
            flips = flip_10_times(coin)
            if coin == 1:
                v1.append(flips)
            if flips < c_min:
                c_min = flips
        v_min.append(c_min)
        randy = flip_10_times(random.randint(1, size+1))
        # random coin?
        v_rand.append(randy)
        if run % 10000 == 0:
            count +=1
            print count
    print "ta-da!"
    print numpy.mean(v_min)
    
    print len(v1), len(v_rand), len(v_min)

    #store the result in a new file
    result_list = [v1, v_rand, v_min]
    newfile = "/Users/timothyroy/Documents/Machine Learning/Hoeffding_results.py"
    import cPickle
    with open(newfile, 'w') as savefile:
      cPickle.dump(result_list, savefile)

    # change to log scale
    pyplot.xscale('log')

    # done
    plt.title ('Log/Log Distribution of Results')
    plt.grid(True)
    plt.xlabel ('Number of flips')
    plt.ylabel ('Number of heads')
    pylab.plot(numpy.arange(number_of_runs), v1)
    pylab.plot(numpy.arange(number_of_runs), v_rand)
    pylab.plot(numpy.arange(number_of_runs), v_min)
    pylab.show()

    return v1, v_rand, v_min 

def flip_10_times (x):
    heads = 0
    # flip each coin 10 times
    for x in xrange(1, 11):
        flip = random.randint(0,1)
        if flip == 1:
            heads += 1
    return heads / float(10)

coinFlip(1000, 100000)
