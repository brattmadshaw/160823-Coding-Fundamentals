input = input("Enter a word: ")

# Initialize counter for vowels
vowel_count = 0

# Iterate through each character
for index in range(len(input)):
    char = input[index]
    
    # Check if the character is a vowel
    if char.lower() in 'aeiou':
        vowel_count += 1
        print(f"{char} at position {index + 1}")

print(f"The number of vowels in '{input}' is: {vowel_count}")
