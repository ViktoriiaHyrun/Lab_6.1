ST1 = input("Enter a string of up to 70 characters: ")

if len(ST1) > 70:
    print("ERROR: The string must contain no more than 70 characters.")
elif len(ST1) < 5:
    print("ERROR: The string must contain at least 5 characters.")
else:
    words = []
    word = ""
    
    for char in ST1:
        if char == ' ':
            if len(word) > 5:
                words.append(word)
            word = ""
        else:
            word += char
    if len(word) > 5:
        words.append(word)
    if len(words) == 0:
        print("ERROR: The string must contain words longer than 5 characters.")
    else:
        print("Words longer than 5 characters:", words)

