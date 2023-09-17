# Define the number of rows
n = 5

# Outer loop to iterate through each row
for i in range(1, n + 1):
    # Inner loop to print asterisks in each row
    for j in range(1, i + 1):
        print("*", end=" ")
    # Move to the next line after printing the row
    print()
