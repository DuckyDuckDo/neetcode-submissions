class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        t = 0
        at_door_enter = [] # use a heap to keep track of minimum guy
        heapq.heapify(at_door_enter)
        at_door_exit = [] # use a heap to keep track of minimum guy
        heapq.heapify(at_door_enter)

        arrivals_dict = defaultdict(list)

        for i, t in enumerate(arrival):
            arrivals_dict[t].append((i, state[i])) # Person, State
        
        res = [None] * len(arrival)
        door_state = 2 # 2 is not used, 0 is opened, 1 is exit
        max_arrival = max(arrival)
        for t in range(max(len(arrival) + 1, max_arrival + len(arrivals_dict[max_arrival]) + 1)):
            for person, state in arrivals_dict[t]:
                if state == 0:
                    heapq.heappush(at_door_enter, (person, state))
                else:
                    heapq.heappush(at_door_exit, (person, state))


            if door_state >= 1:
                if at_door_exit:
                    person, state = heapq.heappop(at_door_exit)
                    res[person] = t
                    door_state = state
                
                elif at_door_enter:
                    person, state = heapq.heappop(at_door_enter)
                    res[person] = t
                    door_state = state
                
                else:
                    door_state = 2
            
            elif door_state == 0:
                if at_door_enter:
                    person, state = heapq.heappop(at_door_enter)
                    res[person] = t
                    door_state = state
                
                elif at_door_exit:
                    person, state = heapq.heappop(at_door_exit)
                    res[person] = t
                    door_state = state
                
                else:
                    door_state = 2
            
            print(t, at_door_enter, at_door_exit, res, door_state)
        
        return res
