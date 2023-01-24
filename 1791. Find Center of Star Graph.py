class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        instances_dict = {}
        for edge in edges:
            if edge[0] not in instances_dict:
                instances_dict[edge[0]] = 1

            if edge[1] not in instances_dict:
                instances_dict[edge[1]] = 1

            if edge[0] in instances_dict:
                instances_dict[edge[0]] = instances_dict[edge[0]] + 1

            if edge[1] in instances_dict:
                instances_dict[edge[1]] = instances_dict[edge[1]] + 1
        
        values = list(instances_dict.values())
        keys = list(instances_dict.keys())
        
        return keys[values.index(max(values))]