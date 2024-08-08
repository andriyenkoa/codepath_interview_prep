from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            row.reverse()

            for i, element in enumerate(row):
                if element == 0:
                    row[i] = 1
                else:
                    row[i] = 0

        return image
