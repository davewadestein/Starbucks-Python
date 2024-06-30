filename = input('Cound words in which file? ')

wordcounts = {} # words and counts stored here

with open(filename) as infile:
    for line in infile: # for each line
        for word in line.lower().split(): # for each word
            if word in wordcounts: # already seen it?
                wordcounts[word] += 1 # increment count
            else: # new word...
                wordcounts[word] = 1 # ...set count to 1

# print out top 10 most frequently occurring words
for word in sorted(wordcounts, key=wordcounts.get, reverse=True)[:10]:
    print(word, wordcounts[word])
