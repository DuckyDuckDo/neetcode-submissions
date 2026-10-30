class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = {
            recipes[i]: ingredients[i] for i in range(len(recipes))
        }


        cache = {s: True for s in supplies}
        def dfs(item):
            if item in cache:
                return cache[item]

            if item not in graph:
                return False 
                
            cache[item] = False
            if item in graph:
                for next_item in graph[item]:
                    if not dfs(next_item):
                        return False
            
            cache[item] = True
            return cache[item]
        
        res = []
        for recipe in graph:
            if dfs(recipe):
                res.append(recipe)
    
        return res
