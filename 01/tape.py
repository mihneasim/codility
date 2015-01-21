# you can use print for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    sum_left = [0]
    sum_right = [0]
    for (ind, elem) in enumerate(A):
        if ind == len(A) - 1:
            continue
        sum_left.append(sum_left[-1] + elem)
    ind = len(A) - 1
    while ind != 0:
        sum_right.insert(0, sum_right[0] + A[ind])
        ind -= 1
    sum_left.pop(0)
    sum_right.pop()
    minimum = abs(sum_left[0]) - abs(sum_right[0])
    min_ind = 0
    #print sum_left
    #print sum_right
    for p in range(len(sum_left)):
        if minimum > abs(sum_left[p]) - abs(sum_right[p]):
            minimum = abs(sum_left[p]) - abs(sum_right[p])
            min_ind = p
    return min_ind + 1

