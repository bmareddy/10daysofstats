import numpy as np

x=list(map(int,list(input().split(' '))))
w = input()
if w:
    w=list(map(int,list(w.split(' '))))

def average(x,weights=None):
    """
    x is array of integers
    w is array of weights corresponding to the integers
    returns weighted average if weights are provided. else returns simple average
    """
    if weights:
        return sum(i*j for i,j in zip(x,weights)) / sum(weights)
    return sum(x) / len(x)

wm = average(x,weights=w)
print(f"{wm:.1f}")

wm = np.average(x,weights=w)
print(f"{wm:.1f}")