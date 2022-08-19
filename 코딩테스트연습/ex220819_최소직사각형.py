# programmers 86491
def solution(sizes):
    max_w, max_h = 0, 0 
    for i,j in sizes:
        if i < j:
            i, j = j, i
        max_w = max(max_w,i)
        max_h = max(max_h,j)
    return max_w * max_h
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))


def solution(sizes):
    return max(max(x) for x in sizes)* max(min(x) for x in sizes)
    # return max([max(x) for x in sizes]) * max([min(x) for x in sizes])
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))


# solution = lambda sizes: max(sum(sizes, [])) * max(min(size) for size in sizes)
def solution(sizes):
    return max(sum(sizes, [])) * max(min(size) for size in sizes)
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))






