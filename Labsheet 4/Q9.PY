import ast

def flatten(items):
    flat = []
    for item in items:
        if isinstance(item, list):
            flat += flatten(item)      # flatten inner list recursively
        else:
            flat.append(item)
    return flat

try:
    nested = ast.literal_eval(input("Enter a nested list, e.g. [1, [2, 3], [4, [5]]]: "))
    if not isinstance(nested, list):
        raise ValueError
    print("Flattened list:", flatten(nested))
except (ValueError, SyntaxError):
    print("Invalid list! Please enter a valid Python list.")