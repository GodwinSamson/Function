def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Example usage
numbers_list = [1, 2, 3, 4, 5]
result = calculate_sum(numbers_list)
print("Sum of the numbers:", result)
