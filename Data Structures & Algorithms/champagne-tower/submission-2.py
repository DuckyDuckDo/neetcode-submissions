class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:

        # Need to keep track of current row and the next row
        curr_row = [poured]
        # While condition is used to ensure that there is still spilling over into next row
        while len(curr_row) - 1 < query_row:
            next_row = [0] * (len(curr_row) + 1) # next row is always just current row length + 1
            # Loop through each row
            for i in range(len(curr_row)):
                # can only split if the split is positive
                new_split = max(0.0, (curr_row[i] - 1) / 2)
                next_row[i] += new_split
                next_row[i + 1] += new_split
            curr_row = next_row
        
        return min(1.0, curr_row[query_glass])
                
