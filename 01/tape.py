# you can use print for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    sums_left = [0]
    sums_right = [0]
    len_a = len(A)

    ind = 0
    while ind != len_a - 1:
        sums_left.append(sums_left[-1] + A[ind])
        ind += 1

    ind = len_a - 1
    while ind != 0:
        sums_right.append(sums_right[-1] + A[ind])
        ind -= 1

    sums_left.pop(0)
    sums_right.pop(0)

    sums_len = len_a - 1
    minimum = abs(sums_left[0] - sums_right[sums_len - 1])
    for p in range(sums_len):
        minimum = min(minimum, abs(sums_left[p] - sums_right[sums_len - 1 - p]))

    return minimum
