class Solution:
    def maximumSwap(self, num: int) -> int:
        string = list(str(num))
        max_from_right = []
        max_so_far, max_index = '0', None
        for i in range(len(string) - 1, -1, -1):
            if string[i] > max_so_far:
                max_so_far = string[i]
                max_index = i
            max_from_right.append([max_so_far, max_index])

        # Loop through max_from_right backwards, if the value > current value, swap with the index
        for i, (max_value, max_index) in enumerate(max_from_right[::-1]):
            if string[i] < max_value:
                string[i], string[max_index] = string[max_index], string[i]
                return int(''.join(string))
        
        return int(''.join(string))
            