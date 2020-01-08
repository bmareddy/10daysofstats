import numpy as np
from scipy import stats

array_x=list(map(int,list(input().split(' '))))

def mode_manual(l):
    """
    l: List of integers
    return mode of list l. if there is more than one mode, then pick lowest
    """
    dict_mode = {}
    for n in l:
        i = l.count(n)
        if i not in dict_mode.keys():
            dict_mode[i] = [n]
        else:
            dict_mode[i].append(n)
    dict_mode = {k: sorted(set(v)) for k,v in dict_mode.items()}
    dict_mode = dict(sorted(dict_mode.items(),key=lambda kv: kv[0], reverse=True))
    keys = list(dict_mode.keys())
    return (dict_mode[keys[0]][0], keys[0])

def median_manual(l):
    """
    l: List of integers
    return median of list l
    """
    n = len(l)
    l = sorted(l)
    if n%2 == 1: return l[int((n-1)/2)]
    return (l[int(n/2)-1] + l[int(n/2)]) / 2

# Manual
mean, median, mode = np.mean(array_x), median_manual(array_x), mode_manual(array_x)
print(f"{mean:.1f}")
print(f"{median:.1f}")
print(f"{mode}") 

# Library
mean, median, mode = np.mean(array_x), np.median(array_x), stats.mode(array_x)
print(f"{mean:.1f}")
print(f"{median:.1f}")
print(f"{mode.mode, mode.count}")