from itertools import combinations

def two_sum(l):
    for var in combinations(l,2):
        if var[0]+var[1]==10:
            print var[0],var[1]
two_sum([-2,12,4,6,5,3,5])