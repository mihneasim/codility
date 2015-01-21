# you can use print for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    sum_left = [0]
    sum_right = [0]

    ind = 0
    while ind != len(A) - 1:
        sum_left.append(sum_left[-1] + A[ind])
        ind += 1

    ind = len(A) - 1
    while ind != 0:
        sum_right.insert(0, sum_right[0] + A[ind])
        ind -= 1

    sum_left.pop(0)
    sum_right.pop()

    minimum = abs(sum_left[0] - sum_right[0])
    for p in range(len(sum_left)):
        minimum = min(minimum, abs(sum_left[p] - sum_right[p]))

    return minimum
