# def group1WinCount(g1, g2):
#     g1.sort()
#     g2.sort()

#     n = len(g1)
#     mod = 10**9 + 7

#     # g1[i] - g2[i] > g2[j] - g1[j]
#     group1 = 0
#     j = 0
#     for i in range(n):
#         while j < n and g1[i] + g1[j] <= g2[i] + g2[j]:
#             j += 1
#         group1 += n - j
#         group1 %= mod
   
#     return group1

from bisect import bisect_right

def group1WinCount(g1, g2):
    n = len(g1)
    mod = 10**9 + 7

    d = [g1[i] - g2[i] for i in range(n)]
    d.sort()

    ans = 0
    for i in range(n):
        if d[i] > 0:
            ans += (n - i - 1)
            if ans > 0: ans %= mod
        else:
            l, r = 0, len(d)
            while l < r:
                mid = (l + r) // 2
                if d[mid] <= -d[i]:
                    l = mid + 1
                else:
                    r = mid
            ans += (n - l) 
            if ans > 0: ans %= mod

    return ans 

if __name__ == '__main__':
    g2 = [1, 2, 3]
    # g1 = [3, 2, 1]
    g1 = [4, 5, 6]
    print(group1WinCount(g1, g2))
