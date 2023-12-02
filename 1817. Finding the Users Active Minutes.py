class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        usr_mins = {}
        for log in logs:
            if not log[0] in usr_mins:
                usr_mins[log[0]] = set()

            usr_mins[log[0]].add(log[1])
        
        usr_mins = {a: len(usr_mins[a]) for a in usr_mins}
        ans = [0] * k

        for log in usr_mins:
            ans[usr_mins[log] - 1] += 1

        return ans
