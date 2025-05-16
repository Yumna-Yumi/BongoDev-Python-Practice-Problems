rhyme = 'Twinkle, twinkle, little star. How I wonder what you are!'
rhyme = rhyme.lower()

freq = {}
for char in rhyme:
    if char.isalpha():
        freq[char] = freq.get(char, 0) + 1

most_frequent = max(freq, key=freq.get)
print("Most frequent character:", most_frequent)