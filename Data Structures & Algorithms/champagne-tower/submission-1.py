class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        curr_row = [poured]
        # While condition is used to ensure that there is still spilling over into next row
        while sum(curr_row) > len(curr_row):
            next_row = [0] * (len(curr_row) + 1)
            # Loop through each row
            for i in range(len(curr_row)):
                new_split = max(0.0, (curr_row[i] - 1) / 2)
                next_row[i] += new_split
                next_row[i + 1] += new_split
            curr_row = next_row

            if (len(curr_row) - 1) == query_row:
                return min(1.0, curr_row[query_glass])

        if query_row >= len(curr_row):
            return 0
        else:
            return min(1.0, curr_row[query_glass])
                
