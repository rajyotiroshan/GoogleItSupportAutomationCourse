import wordcloud

#uninteresting word list and set
uninterestingWordList = ["a","an","the","in","on","at","upon","to","for","if","then","there","this","that","those","these"]
uninterestingWords =set(uninterestingWordList)

inputTextFile = '''Project Gutenberg is a library of over 60,000 free eBooks.
Choose among free epub and Kindle eBooks, download them or read them online.
You will find the world's great literature here, with focus on older works for which U.S.
copyright has expired. Thousands of volunteers digitized and diligently proofread the eBooks, for enjoyment and education.
No fee or registration! Everything from Project Gutenberg is gratis, libre, and completely without cost to readers.
If you find Project Gutenberg useful, please consider a small donation, to help Project Gutenberg digitize more books, maintain our online presence, and improve Project Gutenberg programs and offerings.\n
Other ways to help include digitizing, proofreading and formatting, recording audio books, or reporting errors.
No special apps needed! Project Gutenberg eBooks require no special apps to read, just the regular Web browsers or eBook readers that are included with computers and mobile devices. There have been reports of sites that charge fees for custom apps, or for the same eBooks that are freely available from Project Gutenberg. Some of the apps might have worthwhile features, but none are required to enjoy Project Gutenberg eBooks.'''

#filter for only aplpha
#return a String with no non alpha character.

def filterForAlpha():
    split_file = inputTextFile.split(" ")
    newFileWordList = []
    #iterate over the word in the split_file
    for word in split_file:
        splitWord = word.split()
        newword = ""
        for c in splitWord:
            if c.isalpha():
                newword += c
        newFileWordList.append(newword)
    return " ".join(newFileWordList)

#check if word belongs to uninterestedWordList
def isUninterested(word):
    return word in uninterestingWords

#generatevfrequencies of words
def generatevFrequencies():
    #dictionary for frequencies
    frequencies = {}
    splitWordList = inputTextFile.split(" ")
    for word in splitWordList:
        if word not in frequencies:
            frequencies[word] = 0
        if not isUninterested(word):
            frequencies[word] += 1
    print(frequencies)
    return frequencies
#generate filteres text file
inputTextFile = filterForAlpha()
print(inputTextFile)
#generate wordcloud
cloud = wordcloud.WordCloud()
cloud.generate_from_frequencies(generatevFrequencies())
cloud.toFile("wordcloud.jpg")
