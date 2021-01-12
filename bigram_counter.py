"""A function count_bigrams() that takes a file name as its only argument and returns a
dictionary mapping each tuple representing a bigram in the given file to the number of times it
occurs in the file’s content..
"""
import string


def count_words(file_name):

    with open(file_name, 'r') as f:
        bigrams = []
        lines = []
        words = []
        # split lines to words
        for line in f:
            lines = line.split()
            for word in lines:
                word = word.strip(string.punctuation)
                word = word.lower()
                words.append(word)

        for i, val in enumerate(words):
            if i+1 < len(words):
                bigrams.append((words[i], words[i+1]))
            else:
                bigrams.append((words[i], words[0]))

        # # calculate the frequency of each word
        freq = {}
        for bigram in bigrams:
            if bigram in freq:
                freq[bigram] += 1
            else:
                freq[bigram] = 1

        return freq


if __name__ == "__main__":
    print(count_words("sonnet14-15.txt"))
