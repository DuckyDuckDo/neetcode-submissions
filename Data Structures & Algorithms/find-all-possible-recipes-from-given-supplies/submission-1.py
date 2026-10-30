class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = {
            recipes[i]: ingredients[i] for i in range(len(recipes))
        }


        cache = {}
        def dfs(item, visited = set()):
            if item in cache:
                return cache[item]

            if (item not in graph and item not in supplies) or item in visited:
                cache[item] = False
                return cache[item]

            visited.add(item)
            if item in graph:
                good_recipe = True
                for next_item in graph[item]:
                    good_recipe = good_recipe and dfs(next_item, visited)
            
                cache[item] = good_recipe
                return cache[item]
            
            cache[item] = True
            return cache[item]
        
        res = []
        for recipe in graph:
            if dfs(recipe, set()):
                res.append(recipe)
        
        return res
