class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:

        val = 0

        for op in operations:
            if op[1] == "+":
                val = val + 1
            elif op[1] == "-":
                val = val - 1
        
        return val