"""
For each run, set f to -1,1, or vice versa. X, again, is [-1,1]x[-1,1],
and we will choose n points of x in X.

Evaluate f on the x points to get the corresponding y points.

Use linear regression to find g and evaluate E_in (the fraction of in-
sample points classified incorrectly. 

1. Construct matrix x and vector y from the data set.

## Choose n points of x in X, randomly
## Set f to -1,1 or vice versa. 
## Evaluate f on the x points to get y points
### use squared error (h(x) - f(x))**2

2. Compute pseudo-inverse X.
3. Return w = pseudo-inverse X * y.

Repeat 1000 times, and take the average of E_in. 
"""
# Construct Matrix X and Vector Y from the data set
## Choose n points of x in X, randomly
## Set f to -1,1 or vice versa. 
## Evaluate f on the x points to get y points.
### use squared error (h(x) - f(x))**2

import random
 
def initialization(N):
 
    """ Create the target function and the training set
   a, b correspond to the function y = a*x + b
   """
 
    random.seed()
    pointX1 = random.uniform(-1, 1)
    pointY1 = random.uniform(-1, 1)
    pointX2 = random.uniform(-1, 1)
    pointY2 = random.uniform(-1, 1)
 
    a = (pointY1-pointY2)/(pointX1-pointX2)
    b = pointY2 - a*pointX2
 
    training_set = []
 
    for i in range(N):
        training_set.append([random.uniform(-1, 1), random.uniform(-1, 1)])
 
    return (a, b, training_set)
 

def compare(a, b, c):
 
    """ return the out_put according to the point c and
   the function y = a*x +b """
 
    y = a*c[0] + b
    if (y > c[1]):
        return 1
    else:
        return -1
 
 
def rank(a, b, C):
 
    """Create the list of the different out_put for
   the training set C"""
 
    l = len(C)
    out_put = []
 
    for i in range(l):
        out_put.append(compare(a, b, C[i]))
 
    return out_put

ir = initialization(5)
print rank (ir[0], ir[1], ir[2])

 
#print rank ()

## Put all x points in a matrix. 
## put all y points in a matrix

# compute pseudo-inverse x. Transpose X, multiply by X,
#  take the inverse, then multiply by X transpose. 

# return pseudo-inverse X * y

# repeat 1000 times, and take the average. Store in a list. 
