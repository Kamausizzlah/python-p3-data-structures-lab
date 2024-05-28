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
    pass
    return [food.get("name") for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    pass
    return [food for food in spicy_foods if food.get("heat_level") > 5]

def print_spicy_foods(spicy_foods):
    pass
    print(
        ("\n").join(
            [
                f"{food.get('name')} ({food.get('cuisine')}) | Heat Level: {'🌶' * food.get('heat_level')}"
                for food in spicy_foods
            ]
        )
    )

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    pass
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    pass
    print(
        ("\n").join(
            [
                f"{food.get('name')} ({food.get('cuisine')}) | Heat Level: {'🌶' * food.get('heat_level')}"
                for food in spicy_foods
                if food.get("heat_level") > 5
            ]
        )
    )

def get_average_heat_level(spicy_foods):
    pass
    heat_levels_sum = sum([food.get("heat_level") for food in spicy_foods])
    return heat_levels_sum / len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    pass
    spicy_foods.append(spicy_food)
    return spicy_foods
