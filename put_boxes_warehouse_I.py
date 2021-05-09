class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        boxes.sort(reverse = True)
        N = len(boxes)

        i = 0
        count = 0
   

        for room in warehouse:
            # Iterate through boxes from largest to smallest
            # Discard boxes that doesn't fit in the current warehouse
            while i < N and boxes[i] > room:
                i += 1
            if i == N:
                return count
            count += 1
            i += 1

        return count