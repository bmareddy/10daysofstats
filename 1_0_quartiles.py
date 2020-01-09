import numpy as np

a = list(map(int,list(input().split(' '))))

def quartiles(l):
    """
    l is an array of integers
    returns a tuple of three integers Q1,Q2,Q3 respectively
    this logic excludes the media value when computing the quartiles
    which is OK for continues distribution but incorrect for normal distribution
    see the discussion here: https://www.hackerrank.com/challenges/s10-interquartile-range/forum/comments/173186
    """
    q2 = np.median(l)
    if q2 in l:
        i = l.index(q2)
        q1,q3 = np.median(l[:i]), np.median(l[i+1:])
    else:
        i = int(len(l)/2)
        q1,q3 = np.median(l[:i]), np.median(l[i:])
    return q1,q2,q3

q1,q2,q3 = quartiles(a)
print(q1)
print(q2)
print(q3)
