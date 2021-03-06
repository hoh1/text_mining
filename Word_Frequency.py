import string
import nltk
from nltk.corpus import stopwords


def process_file(filename):
    """Makes a histogram that contains the words from a file.
    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = open(filename)
        
    for line in fp:
        for word in line.split():
            word = word.lower()

            #update the histogram
            hist[word] = hist.get(word, 0) + 1
        
    return hist

def clean_hist(hist):
    
    stop_words = stopwords.words('english')
    new_hist = hist.copy()
    for word in new_hist.keys():
        if word in stop_words:
            new_hist[word]=0
    return new_hist

def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    return sum(hist.values())


def different_words(hist):
    """Returns the number of different words in a histogram."""
    return len(hist)

def most_common(hist):
    """Makes a list of word-freq pairs in descending order of frequency.
    hist: map from word to frequency
    returns: list of (frequency, word) pairs
    """
    temp = []
    for word, frequency in hist.items():
        temp.append((frequency, word))
    
    temp.sort() # only sogrts first elements in the list
    temp.reverse()
    return temp

def main(filename):
    sentence = filename
    hist = process_file(filename)
    print('Total number of words:', total_words(hist))
    print('Number of different words:', different_words(hist))
    hist_after_removing_stopwords = clean_hist(hist)
    t = most_common(hist_after_removing_stopwords)
    print('The most common words are:')
    for freq, word in t[0:20]:
        print(word, '\t', freq)



main('review_combined.txt')
