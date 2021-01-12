"""A function count_words() that takes a file name as its only argument and
returns a dictionary mapping each word in the given file to the number of times it occurs in the
file’s content.
"""
import string


def count_words(file_name):

    with open(file_name, 'r') as f:
        dictionary = {}
        lines = []
        words = []
        # split lines to words
        for line in f:
            lines = line.split()
            for word in lines:
                word = word.strip(string.punctuation)
                word = word.lower()
                words.append(word)

        # # calculate the frequency of each word
        freq = {}
        for word in words:
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1

        return freq


if __name__ == "__main__":
    print(count_words("sonnet14-15.txt"))
