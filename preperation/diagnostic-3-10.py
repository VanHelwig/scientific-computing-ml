def mean(values: list[float]) -> float:
    count = len(values)
    sum_values = 0
    for value in values:
        sum_values += value
    if count == 0:
        raise ValueError("Input list is empty")
    return sum_values / count

# Conceptual questions:
# A. Time Complexity: The time complexity of the mean function is O(n), where n is the number of elements in the input list. This is because we iterate through the entire list once to calculate the sum of the values.
# B. Space Complexity: The space complexity of the mean function is O(1), as we are using a constant amount of additional space regardless of the size of the input list.
# C. Edge Cases: The function raises a ValueError if the input list is empty, which is an important edge case to handle. Other edge cases could include lists with very large or very small floating-point numbers, 
#    but the function should handle those without issue as long as they are valid floats. Negative numbers are also handled correctly, as they will contribute to the sum and mean 
#    calculation just like positive numbers.