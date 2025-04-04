"""
Word Occurrences
Estimate: 15 minutes
Actual:   13 minutes
"""
word_to_count = {}
text = input("Text: ")

words = text.split()
for word in words:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = word
        word_to_count[word] = 1


words = list(word_to_count.keys())
words.sort()
max_length = max((len(word) for word in words))
for word in words:
    print(f"{word:{max_length}} : {word_to_count[word]}")
print(word_to_count)
