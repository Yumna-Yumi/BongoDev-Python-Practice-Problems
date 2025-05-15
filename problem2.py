def count_vowels(sentence):
    vowels = "aeiou"
    count = 0
    for char in sentence.lower():
        if char in vowels:
            count += 1
    return count

print(count_vowels("Data Science is awesome"))  