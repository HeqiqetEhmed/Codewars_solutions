#link https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python

def duplicate_count(text):
    # Convert the input text to lowercase to ensure case-insensitivity
    # Use a generator expression to iterate over each unique character in the lowercase text
    # The 'set' function removes duplicate characters, so each character is counted only once
    # 'count(i)' returns the number of occurrences of character 'i' in the lowercase text
    # The condition 'count(i) > 1' checks if the character appears more than once
    # 'sum(...)' adds up all the True values (which are treated as 1) to get the total count
    return sum(text.lower().count(i) > 1 for i in set(text.lower()))
