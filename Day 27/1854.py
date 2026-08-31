class Solution:
    def maximumPopulation(self, logs: list[list[int]]) -> int:
        year_changes = [0] * 101

        for birth, death in logs:
            year_changes[birth - 1950] += 1
            year_changes[death - 1950] -= 1

        max_pop = 0
        cur_pop = 0
        earliest_year = 1950

        for i in range(101):
            cur_pop += year_changes[i]
            if cur_pop > max_pop:
                max_pop = cur_pop
                earliest_year = 1950 + i

        return earliest_year
