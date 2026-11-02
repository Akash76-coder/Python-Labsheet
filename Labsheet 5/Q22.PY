import ast

def flatten(t):
    flat = ()
    for item in t:
        flat += flatten(item) if isinstance(item, tuple) else (item,)
    return flat

try:
    nested = ast.literal_eval(input("Enter a nested tuple, e.g. (1, (2, 3), (4, (5, 6))): "))
    if not isinstance(nested, tuple):
        raise ValueError
    print("Flattened tuple:", flatten(nested))
except (ValueError, SyntaxError):
    print("Invalid tuple! Please enter a valid Python tuple.")