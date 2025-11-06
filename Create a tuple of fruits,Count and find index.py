fruits = ("apple", "banana", "orange", "apple", "mango", "banana")
fruit = input("Enter a fruit name: ")
count = fruits.count(fruit)
if fruit in fruits:
    index = fruits.index(fruit)
    print(f"'{fruit}' appears {count} time(s) at index {index}.")
else:
    print(f"'{fruit}' not found in the tuple.")
