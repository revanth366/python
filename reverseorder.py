n = int(input("Enter number of items: "))
items = []
for i in range(n):
    item = input(f"Enter item {i+1}: ")
    items.append(item)
print("\nReversed list:")
for item in reversed(items):
    print(item)
