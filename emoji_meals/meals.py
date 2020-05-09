import json
import pkg_resources

RECIPE_PATH = pkg_resources.resource_filename('emoji_meals', 'recipes.json')

# Pre-sort the recipes for a constant-time lookup
with open(RECIPE_PATH, 'r') as fp:
    recipes = json.load(fp)
    sorted_recipes = {}
    for recipe, result in recipes.items():
        sorted_recipes[''.join(sorted(recipe))] = result

def mealify(*args):
    recipe = "".join(sorted("".join([arg for arg in args])))
    try:
        return sorted_recipes[recipe]
    except KeyError:
        return None
