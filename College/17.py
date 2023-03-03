# List ordinal value of each element of a word (Hint: use ord() to get ordinal values)
list_words = ["apple"]
list_ordinals = [ord(i) for x in list_words for i in x]
print("All list ",list_words)
print("Ordinal list ",list_ordinals)