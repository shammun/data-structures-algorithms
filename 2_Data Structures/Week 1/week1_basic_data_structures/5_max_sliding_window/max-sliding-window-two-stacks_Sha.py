class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.max_stack or val >= self.max_stack[-1]:
            self.max_stack.append(val)
    
    def pop(self):
        if self.stack:
            val = self.stack.pop()
            if val == self.max_stack[-1]:
                self.max_stack.pop()
            return val
        return None
    
    def max(self):
        return self.max_stack[-1] if self.max_stack else None

class QueueWithTwoStacks:
    def __init__(self):
        self.stack1 = MaxStack()
        self.stack2 = MaxStack()

    def enqueue(self, val):
        self.stack1.push(val)

    def dequeue(self):
        if not self.stack2.stack:
            while self.stack1.stack:
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

    def max(self):
        max1 = self.stack1.max()
        max2 = self.stack2.max()
        if max1 is None:
            return max2
        if max2 is None:
            return max1
        return max(max1, max2)

def max_sliding_window_efficient(sequence, m):
    queue = QueueWithTwoStacks()
    result = []

    # Initiate the first window
    for i in range(m):
        queue.enqueue(sequence[i])

    # Process all the windows
    for i in range(len(sequence) - m + 1):
        result.append(queue.max())

        # Now remove the first element of this window and add the next item 
        # so that we can move to the next window
        if i < len(sequence) - m: # this ensures that we are not in the last window
            queue.dequeue()
            queue.enqueue(sequence[i + m])

    return result

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_efficient(input_sequence, window_size))
