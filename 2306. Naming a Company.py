class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        valid_names = 0

        for idea_a in ideas:

            for idea_b in ideas:
                if not idea_a is idea_b:
                    if idea_a[0] == idea_b[0]:
                        continue

                    conc_1 = idea_a[0] + idea_b[1:] 
                    conc_2 = idea_b[0] + idea_a[1:]

                    if conc_1 in ideas or conc_2 in ideas:
                        continue
                    else:
                        valid_names += 1

        return valid_names  