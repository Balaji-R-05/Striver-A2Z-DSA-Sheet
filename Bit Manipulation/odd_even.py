def odd_even(n):
    return n&1

if __name__ == "__main__":
    n = 6
    ans = odd_even(n)
    if ans:
        print("ODD")
    else:
        print("EVEN")