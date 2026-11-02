t = tuple(input("Enter items separated by spaces: ").split())
if not t:
    raise SystemExit("The tuple is empty.")

start = int(input("Start index: "))
stop = int(input("Stop index (excluded): "))
step = int(input("Step (non-zero): "))
if step == 0:
    print("Step cannot be zero.")
else:
    print(f"t[{start}:{stop}:{step}] =", t[start:stop:step])