# method_1
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return not (
            rec1[0] >= rec2[2] or
            rec1[2] <= rec2[0] or
            rec1[1] >= rec2[3] or
            rec1[3] <= rec2[1]
        )
# method_2
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return (
            min(rec1[2], rec2[2]) > max(rec1[0], rec2[0]) and
            min(rec1[3], rec2[3]) > max(rec1[1], rec2[1])
        )