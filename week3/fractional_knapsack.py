# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    valueperweight = []
    for i in range(len(weights)):
        valueperweight.append([values[i], weights[i],values[i]/weights[i]])
    valueperweight.sort(key = lambda x: x[2])
    # print(valueperweight)
    while capacity >0 and len(valueperweight)>0 :
        element = valueperweight.pop()
        # print(element)
        weight = element[1]
        v = element[0]
        if weight <= capacity:
            # print(v)
            value += v
            capacity -= weight
        else:
            value += (capacity/weight)*v
            capacity = 0
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
