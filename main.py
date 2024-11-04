
def reverse(text: str) -> str:
    return text[::-1]

def first_letter_big(text: str) -> str:
    return text[0].upper() + text[1:].lower()

def bubblesort(l: list) -> list:
    n: int = len(l)
    for i in range(n):
        for j in range(n - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l

def linearSearch(l: list, c: int) -> int:
    for i in range(len(l)):
        if l[i] == c:
            return i
    return -1

def binarySearch(l: list, c: int) -> int:
    n: int = len(l)
    L: int = 0
    R: int = n - 1
    
    while L < R:
        M: int = (L + R) // 2
        if l[M] == c:
            return M
        elif l[M] < c:
            L: int = M
        elif l[M] > c:
            R: int = M
    return -1

def maxHeap(l: list, n: int, i: int):
    largest: int = i
    left: int = i*2+1
    right: int = i*2+2
    
    if left < n and l[left] > l[largest]:
        largest: int = left
    if right < n and l[right] > l[largest]:
        largest: int = right
    if largest != i:
        l[largest], l[i] = l[i], l[largest]
        maxHeap(l, n, largest)

def heapSort(l: list) -> list:
    n: int = len(l)
    for i in range(n // 2 - 1, -1, -1):
        maxHeap(l, n, i)
    for i in range(n-1, 0, -1):
        l[0], l[i] = l[i], l[0]
        maxHeap(l, i, 0)
    return l

def check(l: list) -> bool:
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            return False
    return True

def heapSortOptimized(l: list) -> list:
    if check(l):
        return l
    L: int = 0
    R: int = n - 1
    while L < R:
        if l[L] < l[R]:
            l[L], l[R] = l[R], l[L]
        L += 1
        R -= 1
    return heapSort(l)