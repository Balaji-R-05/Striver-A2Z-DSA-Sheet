def isPowerOfTwo(n):
    count = 0
    while n>0:
        count += n&1
        n>>=1
    return count == 1

if __name__ == "__main__":
    n = 16
    res = isPowerOfTwo(n)
    if res:
        print(f"{n} is a power of 2")
    else:
        print(f"{n} is not a power of 2")