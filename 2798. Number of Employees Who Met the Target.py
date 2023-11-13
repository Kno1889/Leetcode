class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count = 0

        for emp_hrs in hours:
            if emp_hrs >= target:
                count += 1
        
        return count
        