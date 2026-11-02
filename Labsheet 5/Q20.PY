t = tuple(input("Enter words separated by spaces: ").split())
if not t:
    raise SystemExit("The tuple is empty.")

longest = max(t, key=len)
print(f"Longest word = '{longest}', length = {len(longest)}")