def bubble_sort(n: int, arr: list[int]) -> list[int]:
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == "__main__":
    arr = [13,46,24,52,20,9]
    res = bubble_sort(len(arr), arr)
    print(res)