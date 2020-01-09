import numpy as np

x = list(input().split(' '))
f = list(map(int,list(input().split(' '))))

def median(l):
    n = len(l)
    if n%2 == 0:
        return (l[int(n/2)]+l[int((n/2))-1]) / 2.0
    return l[int((n-1)/2)]

def quartiles(l):
    """
    l is an array of integers
    returns a tuple of three integers Q1,Q2,Q3 respectively
    """
    q2 = median(l)
    n = len(l)
    if n%2 != 0:
        i = int((n-1)/2)
        q1,q3 = median(l[:i]), median(l[i+1:])
    else:
        i = int(n/2)
        q1,q3 = median(l[:i]), median(l[i:])
    return q1,q2,q3

s = [int(i) for i,j in zip(x,f) for _ in range(j)]
q1,q2,q3 = quartiles(sorted(s))
#print(q1,q2,q3)
print("{0:.1f}".format(q3-q1))

# Needless to say, this is correct. The above answer is incorrect due to
# https://www.hackerrank.com/challenges/s10-interquartile-range/forum/comments/173186
q1,q2,q3 = np.percentile(s,25), np.percentile(s,50), np.percentile(s,75)
#print(q1,q2,q3)
print("{0:.1f}".format(q3-q1))
