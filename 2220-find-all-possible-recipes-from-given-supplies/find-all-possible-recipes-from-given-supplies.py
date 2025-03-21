from collections import deque, defaultdict
from typing import List

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        indegree = defaultdict(int)
        graph = defaultdict(list)
        available = set(supplies)
        result = []

        for recipe, ingredient_list in zip(recipes, ingredients):
            indegree[recipe] = len(ingredient_list)
            for ing in ingredient_list:
                graph[ing].append(recipe)

        queue = deque(supplies)

        while queue:
            ingredient = queue.popleft()
            if ingredient in recipes:
                result.append(ingredient)

            for recipe in graph[ingredient]:
                indegree[recipe] -= 1
                if indegree[recipe] == 0:
                    queue.append(recipe)
        
        return result
