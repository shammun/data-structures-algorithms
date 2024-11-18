class Heap:
    def __init__(self):
        self.heap = []
    
    def heapify(self, arr):
        self.heap = arr
        swaps = []
        size = len(self.heap)

        for i in range(size // 2 - 1, -1, -1):
            j = i
            while True:
                largest = j
                left = 2*j + 1
                right = 2*j + 2

                if left < size and self.heap[left] < self.heap[largest]:
                    largest = left
                if right < size and self.heap[right] < self.heap[largest]:
                    largest = right
                
                if largest != j:
                    self.heap[j], self.heap[largest] = self.heap[largest], self.heap[j]
                    swaps.append((j, largest))
                    j = largest
                else:
                    break

        return swaps

def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    heap = Heap()
    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)
    

def build_heap(data):
    heap = Heap()
    swaps = heap.heapify(data)
    return heap.heap, swaps

def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    _, swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    # run_tests()
    main()