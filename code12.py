sentence = input("Enter a sentence: ")

words = sentence.split()

word_lengths = []
for word in words:
  word_lengths.append(len(word))

print(word_lengths)