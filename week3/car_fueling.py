# python3
import sys


def compute_min_refills(distance, tank, stops):
    stops.append(distance)
    visited =0
    travel = 0
    i = 0
    prev = 0
    while i < len(stops):
        # print(travel)
        if stops[i] <= travel+tank:
            if i == len(stops):
                break
            prev = i
            i+=1
        else:
            if stops[prev] == travel:
                return -1
            visited +=1
            travel = stops[prev]
    travel

        


    return visited
    


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
