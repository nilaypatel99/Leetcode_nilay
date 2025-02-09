import heapq

class NumberContainers:
    def __init__(self):
        self.index_map = {}  # Maps index -> number
        self.num_map = {}  # Maps number -> min_heap of indices
        self.valid_indices = {}  # (index -> number), helps with lazy deletion

    def change(self, index: int, number: int) -> None:
        if index in self.index_map:
            old_number = self.index_map[index]
            if old_number in self.num_map:
                self.valid_indices[(index, old_number)] = False  # Mark old index as invalid
        
        # Update the new number at index
        self.index_map[index] = number
        self.valid_indices[(index, number)] = True  # Mark index as valid

        # Add index to min-heap for the new number
        if number not in self.num_map:
            self.num_map[number] = []
        heapq.heappush(self.num_map[number], index)

    def find(self, number: int) -> int:
        if number not in self.num_map:
            return -1

        min_heap = self.num_map[number]
        while min_heap:
            smallest_index = min_heap[0]
            if self.valid_indices.get((smallest_index, number), False):
                return smallest_index
            heapq.heappop(min_heap)  # Remove invalid index

        return -1
