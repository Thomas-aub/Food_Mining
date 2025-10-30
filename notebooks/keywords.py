"""
keywords.py
Food and cuisine keyword mappings for cluster purity and theme detection.
"""

# Cuisine, theme, and cross-category culinary keyword lists
CUISINE_KEYWORDS = {
    # --- Regional Cuisines ---
    "italian": [
        "parmesan", "mozzarella", "ricotta", "pasta", "spaghetti", "penne",
        "basil", "oregano", "rosemary", "olive oil", "pesto", "bolognese",
        "alfredo", "carbonara", "prosciutto", "pancetta", "salami", "risotto"
    ],
    "chinese": [
        "soy sauce", "hoisin", "oyster sauce", "black bean", "bok choy",
        "chow mein", "wonton", "dumpling", "ginger", "sichuan", "five spice",
        "chili oil", "rice vinegar", "stir fry", "sesame oil"
    ],
    "japanese": [
        "soy sauce", "miso", "ramen", "sushi", "nori", "ponzu", "wasabi", "sake",
        "teriyaki", "tempura", "panko", "daikon", "kombu", "shoyu"
    ],
    "thai": [
        "lemongrass", "galangal", "kaffir lime", "fish sauce", "red curry", "green curry",
        "massaman", "panang", "tamarind", "thai basil", "coconut milk", "sticky rice",
        "pad thai", "shrimp paste", "chili paste"
    ],
    "indian": [
        "garam masala", "turmeric", "cumin", "coriander", "cardamom", "fenugreek",
        "paneer", "ghee", "yogurt", "lentil", "dal", "naan", "chutney", "tikka",
        "biryani", "samosa", "raita", "masala"
    ],
    "mexican": [
        "taco", "tortilla", "salsa", "guacamole", "avocado", "cilantro", "lime",
        "jalapeño", "nacho", "queso", "corn", "beans", "mole", "chili powder", "cumin"
    ],
    "french": [
        "butter", "cream", "wine", "tarragon", "thyme", "shallot", "baguette",
        "croissant", "béchamel", "roux", "duck", "brie", "gruyere", "pâté"
    ],
    "middle_eastern": [
        "hummus", "falafel", "tahini", "pita", "lamb", "chickpea", "couscous",
        "harissa", "zaatar", "mint", "sumac", "pomegranate", "olive oil"
    ],
    "vietnamese": [
        "fish sauce", "pho", "banh mi", "vermicelli", "sriracha", "mint",
        "lemongrass", "cilantro", "bean sprout", "nuoc mam"
    ],
    "korean": [
        "kimchi", "gochujang", "doenjang", "bulgogi", "galbi", "sesame oil",
        "garlic", "soy sauce", "rice cake", "green onion"
    ],
    "greek": [
        "feta", "olive", "oregano", "cucumber", "lemon", "yogurt", "tzatziki",
        "phyllo", "spinach", "lamb", "souvlaki"
    ],
    "spanish": [
        "paella", "saffron", "chorizo", "tapas", "gazpacho", "olive oil", "paprika"
    ],
    "moroccan": [
        "cumin", "cinnamon", "turmeric", "ras el hanout", "tagine", "couscous",
        "preserved lemon", "chickpea", "mint"
    ],
    "brazilian": [
        "feijoada", "black beans", "cassava", "linguiça", "palm oil", "coconut milk",
        "okra", "mango", "passion fruit"
    ],

    # --- Cross-category Themes ---
    "baking": [
        "flour", "sugar", "butter", "egg", "yeast", "baking powder",
        "baking soda", "dough", "bread", "cake", "cookie", "pie crust",
        "icing", "pastry", "brown sugar", "vanilla extract"
    ],
    "dessert": [
        "chocolate", "cream", "ice cream", "caramel", "custard", "pudding",
        "marshmallow", "syrup", "mousse", "brownie", "tart", "honey"
    ],
    "breakfast": [
        "pancake", "oats", "muffin", "toast", "waffle", "omelette",
        "coffee", "cereal", "bagel", "juice"
    ],
    "vegan": [
        "tofu", "tempeh", "soy milk", "seitan", "lentil", "beans", "chia",
        "flaxseed", "coconut milk", "almond milk"
    ],
    "vegetarian": [
        "tofu", "paneer", "cheese", "milk", "vegetable broth", "spinach",
        "broccoli", "zucchini", "tomato"
    ],
    "snack": [
        "popcorn", "chips", "nuts", "granola", "crackers", "nachos", "trail mix"
    ],
    "salad": [
        "lettuce", "arugula", "spinach", "kale", "avocado", "vinaigrette",
        "olive oil", "balsamic", "feta"
    ],
    "soup": [
        "broth", "stock", "stew", "minestrone", "ramen", "chowder", "miso soup"
    ],
    "sandwich": [
        "bread", "ham", "turkey", "cheese", "mayonnaise", "tomato", "lettuce"
    ],
    "pasta": [
        "spaghetti", "penne", "pesto", "alfredo", "bolognese", "lasagna", "carbonara"
    ],
    "rice_dish": [
        "fried rice", "risotto", "paella", "biryani", "jambalaya", "pilaf"
    ],
    "grill_bbq": [
        "barbecue", "bbq", "grill", "ribs", "steak", "burger", "brisket", "kebab"
    ],
    "noodle": [
        "ramen", "lo mein", "vermicelli", "udon", "spaghetti", "glass noodle"
    ],
    "seafood": [
        "shrimp", "crab", "lobster", "fish", "tuna", "salmon", "clam", "oyster"
    ],
    "meat": [
        "beef", "chicken", "pork", "duck", "sausage", "steak", "meatball"
    ],
    "drink": [
        "coffee", "tea", "juice", "smoothie", "cocktail", "beer", "wine", "soda"
    ],
    "sauce_condiment": [
        "ketchup", "mustard", "mayonnaise", "soy sauce", "pesto", "gravy",
        "ranch", "bbq sauce", "aioli"
    ],
    "pizza": [
        "mozzarella", "tomato sauce", "pepperoni", "margherita", "basil", "crust"
    ],
    "burger": [
        "bun", "patty", "cheese", "onion", "pickle", "ketchup", "mustard"
    ],
    "stir_fry": [
        "wok", "soy sauce", "ginger", "garlic", "sesame oil", "bell pepper"
    ]
}

def get_keywords():
    """Return the unified cuisine and theme keyword dictionary."""
    return CUISINE_KEYWORDS
