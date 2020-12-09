class Solution:
    def merge(self, intervals):
        aux = sorted(intervals)
        merged = [aux[0]]

        for cur_int in aux[1:]:

            start, end = cur_int[0], cur_int[1]
            
            last_start, last_end = merged[-1]
            if (start <= last_end):
                
                merged[-1] = [last_start, max(last_end, end)]
            else:
                merged.append([start, end])

        return merged