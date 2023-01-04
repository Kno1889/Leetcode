class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        completed_tasks = []
        min_rounds = 0

        for task in tasks:
            if task not in completed_tasks:
                if tasks.count(task) == 2 or tasks.count(task) == 3:
                    completed_tasks.append(task)
                    min_rounds = min_rounds + 1
                else:
                    return -1
        return min_rounds
        