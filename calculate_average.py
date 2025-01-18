def calculate_average(numbers):
    total_sum = sum(numbers)
    count = len(numbers)
    average = total_sum / count
    return average


result = calculate_average([1, 2, 3, 4, 5])
print(result)


print(calculate_average([]))  # Output: 0

print(calculate_average([1, "a", 3]))
# Output: ValueError: All elements in 'numbers' must be integers or floats

print(calculate_average("12345"))
# Output: TypeError: Input must be a list or tuple of numbers
