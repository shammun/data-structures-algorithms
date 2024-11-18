class Heap:
    def __init__(self):
        self.heap = [0]
    
    def insert(self, val):
        # append to the end of the heap
        self.heap.append(val)
        i = len(self.heap) - 1
        # Percolate up
        # While there is a parent of the current node 
        # and the parent is larger than the current node
        while i > 1 and self.heap[i] < self.heap[i//2]:
            tmp = self.heap[i]
            self.heap[i] = self.heap[i//2]
            self.heap[i//2] = tmp
            i = i // 2
        
    def pop(self):
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()
        
        res = self.heap[1]
        self.heap[1] = self.heap.pop()
        i = 1
        # Percolate down
        # While there is a left child
        while 2 * i < len(self.heap):
            # Check whether there is a right child and if it is smaller than 
            # the root and smaller than the left child
            if (2 * i + 1 < len(self.heap)) and self.heap[2*i + 1] < self.heap[i] and self.heap[2*i + 1] < self.heap[2*i]:
                # Swap right child
                tmp = self.heap[i]
                self.heap[i] = self.heap[2*i + 1]
                self.heap[2*i + 1] = tmp
                i = 2*i + 1
            elif self.heap[2 * i] < self.heap[i]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[2 * i]
                self.heap[2 * i] = tmp
                i = 2 * i
            else:
                break
        return res 
        
    def peek(self):
        if len(self.heap) == 1:
            return None
        return self.heap[1]
    
    def heapify(self, arr):
        # Move element at 0th position to the end of the array/heap
        # Then percolate down
        arr.append(arr[0])
        self.heap = arr 
        cur = (len(self.heap) - 1) // 2
        while cur > 0:
            i = cur 
            while 2 * i < len(self.heap):
                if (2*i + 1 < len(self.heap)) and self.heap[2*i + 1] < self.heap[i] and self.heap[2*i + 1] < self.heap[2*i]:
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2*i + 1]
                    self.heap[2*i + 1] = tmp
                    i = 2 * i + 1
                elif self.heap[2*i] < self.heap[i]:
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2*i]
                    self.heap[2*i] = tmp
                    i = 2* i
                else:
                    break
            cur -= 1

def parallel_processing(n, m, jobs):
    result = []

    threads = Heap()
    for i in range(n):
        threads.insert((0, i))

    for i, job_time in enumerate(jobs):
        next_available_time, thread_index = threads.pop()

        result.append((thread_index, next_available_time))
        threads.insert((next_available_time + job_time, thread_index))
    
    return result

"""
def parallel_processing(n, m, jobs):
    # Initialize the output list
    result = []
    
    # Initialize a min heap to keep track of thread availability
    # Each item in the heap is a tuple (next_available_time, thread_index)
    threads = Heap()
    for i in range(n):
        threads.insert((0, i))
    
    # Process each job
    for i, job_time in enumerate(jobs):
        # Get the next available thread
        next_available_time, thread_index = threads.pop()
        
        # Add the job to the result
        result.append((thread_index, next_available_time))
        
        # Update the thread's next available time and put it back in the heap
        threads.insert((next_available_time + job_time, thread_index))
    
    return result
"""


def main():
    n, m = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert m == len(jobs)

    # Process jobs
    schedule = parallel_processing(n, m, jobs)

    # Print output
    for thread_index, start_time in schedule:
        print(thread_index, start_time)


if __name__ == "__main__":
    main()