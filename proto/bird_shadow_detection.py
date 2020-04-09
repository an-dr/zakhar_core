import numpy as np
import collections


def cc(a, b):
    return np.corrcoef(a, b)[1, 0]


def get_cc(pattern: list, mon_window: collections.deque, new_val):
    if len(pattern) != len(mon_window):
        raise TypeError("Pattern should be the same length as a monitored window")
    mon_window.append(new_val)
    return np.corrcoef(pattern, mon_window)[1, 0]


if __name__ == '__main__':
    pattern = [0, 0, 0, 1, 0, 0, 0]  # let say, 1 sec
    signal1 = [200, 201, 205, 210, 220, 230, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200]
    signal2 = [200, 201, 205, 500, 220, 230, 200, 201, 200, 200, 201, 200, 200, 202, 200, 200]

    size = len(pattern)
    # size = 10
    window = collections.deque([0] * size, maxlen=size)  # 0.1sec x 10

    i = 0
    while (i < len(signal2)):
        c = get_cc(pattern, window, signal2[i])
        # window.append(signal1[i])
        print("Corr coefficient: " + str(c))
        i += 1

    print("[ DONE ]")

    # print("Corr coefficients pattern vs s2: " + str(cc(signal2, pattern)))
