class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if poured == 0:
            return 0

        curr_row = [poured]
        while sum(curr_row) > len(curr_row):
            next_row = [0] * (len(curr_row) + 1)
            for i in range(len(curr_row)):
                if curr_row[i] <= 1:
                    continue
                new_split = (curr_row[i] - 1) / 2
                next_row[i] += new_split
                next_row[i + 1] += new_split
            curr_row = next_row

            if (len(curr_row) - 1) == query_row:
                return 1 if curr_row[query_glass] >= 1 else curr_row[query_glass]

        if query_row >= len(curr_row):
            return 0
        else:
            return 1 if curr_row[query_glass] >= 1 else curr_row[query_glass]
                
