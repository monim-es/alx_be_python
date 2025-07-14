# pattern_drawing.py

# Prompt the user for the pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer loop: while loop for rows
while row < size:
    # Inner loop: for loop for columns
    for col in range(size):
        print("*", end="")
    print()  # Move to next line after each row
    row += 1
