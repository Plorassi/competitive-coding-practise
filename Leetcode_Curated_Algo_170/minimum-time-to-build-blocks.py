class Solution:
    def minBuildTime(self, blocks: List[int], split: int) -> int:
        heapq.heapify(blocks)

        while len(blocks) > 1:
            heapq.heappop(blocks)
            second_smallest_block = heapq.heappop(blocks)
            heapq.heappush(blocks, split+second_smallest_block)

        return blocks[0]
