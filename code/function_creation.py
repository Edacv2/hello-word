print('Hi User,')
def character_count(s):
    """This will count the amount of character in any given word"""
    count_character = len(s)
    print("The amount of characters are:", count_character)

word = input('Please enter a word: ')
character_count(word)

# Run print(character_count.__doc__) to get Docstring (line 3).