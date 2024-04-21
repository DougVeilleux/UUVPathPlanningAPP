#MinIndexPriorityQueue.py
"""
A min-index priority queue data structure combines the features of a priority
queue and an indexing data structure.  It allows for efficient retrival of the
minimum element, as well as updating the priority of elements.




"""

import heapq
class MinIndexPriorityQueue:
    """
    This "min-inded queue" implementation uses 'heap' to store the elements
    with their priorities, and the 'index' is a dictionary mapping elements
    to their positions in the heap.  'counter' is used to ensure that elements
    inserted at the same priority level are ordered based on their insertion order.
    """
    def __init__(self):
        self.heap = []
        self.index = {}
        self.counter = 0

    def insert(self, item, priority):
        self.counter += 1
        entry = [priority, self.counter, item]
        self.index[item] = entry
        heapq.heappush(self.heap, entry)

    def get(self):
        while self.heap:
            priority, _, item = heapq.heappop(self.heap)
            if item is not None:
                del self.index[item]
                return priority, item
        raise IndexError("pop from an empty priority queue")

    def contains(self, item):
        return item in self.index

    def delete(self, item):
        entry = self.index.pop(item)
        entry[-1] = None

    def decrease_key(self, item, new_priority):
        if item in self.index:
            entry = self.index[item]
            entry[0] = new_priority
            heapq.heapify(self.heap)
        else:
            raise ValueError(f"Item '{item}' not found in priority queue")
    def extract_min(self):
        while self.heap:
            priority, _, item = heapq.heappop(self.heap)
            if item is not None:
                del self.index[item]
                return item, priority
        raise IndexError("pop from an empty priority queue")

    def is_empty(self):
        return len(self.heap) == 0


if __name__ == '__main__':
    # Create an instance of MinIndexPriorityQueue
    priority_queue = MinIndexPriorityQueue()

    # Insert elements into the priority queue
    priority_queue.insert("Task 1", 5)
    priority_queue.insert("Task 2", 3)
    priority_queue.insert("Task 3", 7)
    priority_queue.insert("Task 4", 2)

    # Print the current state of the priority queue
    print("Current state of the priority queue:")
    while not priority_queue.is_empty():
        item, priority = priority_queue.extract_min()
        print(f"Item: {item}, Priority: {priority}")

    # Update priority of an item
    priority_queue.insert("Task 5", 8)
    priority_queue.decrease_key("Task 3", 4)

    # Print the current state of the priority queue
    print("\nUpdated state of the priority queue:")
    while not priority_queue.is_empty():
        item, priority = priority_queue.extract_min()
        print(f"Item: {item}, Priority: {priority}")

