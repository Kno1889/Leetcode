class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image[0])
        for row in image:
            row.reverse()

        for row in image:
            for i in range(n):
                if row[i] == 0:
                    row[i] = 1
                else:
                    row[i] = 0
        return image
