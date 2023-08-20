spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    hot_foods = []
    for food in spicy_foods:
        hot_foods.append(food["name"])
    return hot_foods

hot_foods = get_names(spicy_foods)
print(hot_foods)

def get_spiciest_foods(spicy_foods):
    spiciest_foods = {}
    for food in spiciest_foods:
        if food['cuisine'] in spiciest_foods:
            spiciest_foods[food['name']] = food['cuisine']
    return spiciest_foods

def print_spicy_foods(spicy_foods):
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    pass

def print_spiciest_foods(spicy_foods):
    pass

def get_average_heat_level(spicy_foods):
    pass

def create_spicy_food(spicy_foods, spicy_food):
    pass
