even_count = 0
odd_count = 0

n = int(input("Enter how many numbers you want to input: "))

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("\nTotal even numbers:", even_count)
print("Total odd numbers:", odd_count)
