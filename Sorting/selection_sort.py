def selection_sort(n: int, arr: list[int]) -> list[int]:
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

if __name__ == "__main__":
    arr = [13,46,24,52,20,9]
    res = selection_sort(len(arr), arr)
    print(res)
