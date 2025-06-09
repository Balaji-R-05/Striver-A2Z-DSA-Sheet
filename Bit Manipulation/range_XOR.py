def findRangeXOR(l, r):
    ans = 0
    for i in range(l, r+1):
        ans ^= i
    return ans

if __name__ == "__main__":
    l, r = 3, 5
    ans = findRangeXOR(l, r)
    print(ans)