def capitalize_words(sentence):
    words = sentence.split()
    capitalized = [word[0].upper() + word[1:] if word else '' for word in words]
    return ' '.join(capitalized)

print(capitalize_words("python for web developers"))  