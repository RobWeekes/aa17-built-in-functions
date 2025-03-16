# Given a list of `Cat` objects (dictionaries representing cats), write a
# function `cat_verify` that uses the `all()` built-in function to determine if
# all cats are the same breed. Then use `any()` to determine if any of them are
# up for adoption. Return the result as a tuple.

# The `breed` represents the cat's breed, and `adopted` represents whether the
# cat bas been adopted already or not.

cat_list = [
    {
        "name": "Lenny",
        "breed": "Ragdoll",
        "adopted": False
    },
    {
        "name": "Roger",
        "breed": "Siamese",
        "adopted": False
    },
    {
        "name": "Katya",
        "breed": "Persian",
        "adopted": True
    }
]

# Write your code here.

# had to make a copy of map_object before converting it to list for printing

def cat_verify(cats):
  map_object = map(lambda cat: cat['breed'] == cats[0]['breed'], cats)
  map_object_copy = map(lambda cat: cat['breed'] == cats[0]['breed'], cats)
  map_object_list = list(map_object_copy)
  print(f'map object: cat breed matches: {map_object_list}')
  cat_breed_list = all(map_object)
  print(f'cat_breed boolean: {cat_breed_list}')  # True, should be False

  up_for_adopt = any(map(lambda cat: cat['adopted'] == False, cats))
  print(f'any up for adoption: {up_for_adopt}')   # True

  return (cat_breed_list, up_for_adopt)   # (False, True) - correct tuple
  # return (cat_breed_list and up_for_adopt)   # False - from lecture recording

print(cat_verify(cat_list))    # False, True


# There's an issue in the current implementation. The map_object is being converted to a list with list(map_object) for printing, which consumes the map iterator. When the code then tries to use all(map_object), the map object is already exhausted, resulting in incorrect behavior.

# def cat_verify(cats):
#   map_object = map(lambda cat: cat['breed'] == cats[0]['breed'], cats)
#   print(f'map object in cat_breed variable: {list(map_object)}')
#   cat_breed = all(map_object)
#   print(f'cat_breed boolean: {cat_breed}')
#   # # one-line version
#   # cat_breed = all(map(lambda cat: cat['breed'] == cats[0]['breed'], cats))

#   # up_for_adopt =


# print(cat_verify(cat_list))    # False
