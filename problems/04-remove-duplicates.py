# Say you took a survey of your class of all the phones, and you want to get all
# the unique phone models.

# First, write a function `get_unique_models` that filters out duplicates of a
# given model. Assume that brands and models are one-to-one, meaning there won't
# be two brands that have same model name.

# Then, write a function `map_to_names` that returns a list of just the model
# names given the list of phones.

phones = [
    {
        "brand": "Apple",
        "model": "iPhone 13 Pro",
        "cost": 929,
        "color": "alpine green"
    },
    {
        "brand": "Samsung",
        "model": "Galaxy S22+",
        "cost": 999,
        "color": "black"
    },
    {
        "brand": "Google",
        "model": "Pixel 6",
        "cost": 599,
        "color": "kinda coral"
    },
    {
        "brand": "Apple",
        "model": "iPhone 13 Pro",
        "cost": 929,
        "color": "gold"
    },
    {
        "brand": "Google",
        "model": "Pixel 6",
        "cost": 599,
        "color": "stormy black"
    }
]

# Write your code here.
def get_unique_models(phone_list):
    seen = []
    return filter(lambda phone: seen.append(phone['model']) is None if phone['model'] not in seen else False, phone_list)

def map_to_names(phone_list):
    return list(map(lambda phone: phone['model'], phone_list))

unique_models = list(get_unique_models(phones))
# print(unique_models)                # iPhone 13 Pro, Galaxy S22+, Pixel 6 (dictionaries)
print(map_to_names(unique_models))  # iPhone 13 Pro, Galaxy S22+, Pixel 6

# implementation of the get_unique_models function:

# seen = [] - Creates an empty list to track which phone models we've already encountered.

# The filter() function takes two arguments:

# A function (in this case, a lambda)
# An iterable (in this case, phone_list)
# The lambda function is the key part:

# lambda phone: seen.append(phone['model']) is None if phone['model'] not in seen else False

# Copy

# Apply

# This works in a non-obvious way:

# First, it checks if phone['model'] not in seen
# If the model hasn't been seen yet:
# It executes seen.append(phone['model']) is None
# seen.append() adds the model to the seen list and returns None
# None is None evaluates to True
# So the phone is included in the filter results
# If the model has been seen:
# It returns False
# So the phone is excluded from the filter results
# The result is that only the first occurrence of each phone model passes through the filter.
