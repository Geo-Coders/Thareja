# Write a program that accepts different numbers of arguments and return the maximum value passed to it

def max_value(*args):
    if not args:
        return None
    else:
        return max(args)


# Example usage
print(f"The maximum number passed to it is : {max_value(1, 3, 5, 7)}") # Output: 7
print(max_value(10, 2, 8))  # Output: 10
print(max_value())  # Output: None
