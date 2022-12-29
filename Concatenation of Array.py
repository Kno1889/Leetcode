def getConcatenation(nums):
     """
     :type nums: List[int]
     :rtype: List[int]
     """
     ans = []

     for num in nums:
          ans.append(num)

     for num in nums:
          ans.append(num)

     return ans

def main():
     print(getConcatenation([1, 2, 1]))

if __name__ == "__main__":
     main()
