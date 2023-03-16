class MinHeap:
    def __init__(self, array):
        self.A = array
        self.size = len(self.A)
        self.swaps = []


    def SiftDown(self, i):
        min_index = i
        left = 2 * i + 1  
        right = 2 * i + 2 
        if left < self.size and self.A[left] < self.A[min_index]:
            min_index = left
        if right < self.size and self.A[right] < self.A[min_index]:
            min_index = right
        if min_index != i:
            self.swaps.append((i, min_index))
            self.A[i], self.A[min_index] = self.A[min_index], self.A[i]
            self.SiftDown(min_index)

    def BuildHeap(self):
        n = self.size
        for i in range(n // 2 - 1, -1, -1):
            self.SiftDown(i)

def readData():

    text = input()
    # Printing answer, write your code here
    if "I" in text:
        print("Please enter numbers of swaps")
        n = int(input())
        print("Please enter array")
        array = list(map(int, input().split()))
        assert len(array) == n
    if "F" in text:
            al="./test/"+input()
            f = open(al, "r")
            n = int(f.readline())
            array = list(map(int, f.readline().split()))
    heap = MinHeap(array)
    MinHeap.BuildHeap(heap)
    swaps = heap.swaps
    print(len(swaps))
    for swap in swaps:
        print(*swap)

    

def main():
    readData()


if __name__ == "__main__":
    main()