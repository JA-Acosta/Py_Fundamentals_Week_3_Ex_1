'''
>>> JAAR
>>> 8/6/2023
>>> Practicing Fundamentals Program 13
>>> Version 1
'''

'''
>>> Generates a program that prints a text file to the console and counts the number of lines in the text file as well as the occurrence of each word in the text file and prints all of the information for the user below the Original text.
'''

import re

def print_word_count(counts : dict) :
    '''
    >>> Prints the number of lines counted as well as the count for each individual word to the console.

    >> Param: (dict) counts
    '''
    print(f'Number of Lines: {counts["line"]}')
    print('Words and Count of each words: ')
    print(', '.join(f"'{w}': {c}" for w, c in counts["word"].items()))
    print(f'Word Total :{sum(counts["word"].values())} ')

def main() :
    counts = { 'line' : 0, 'word' : {}}
    with open('the_little_prince.txt', 'r') as story :
        for line in story.readlines() :
            print(line, end= '')
            line = line.lower()
            counts['line'] += 1
            w = re.compile(r"\b[a-zA-Z]+'?[a-zA-Z]*\b")
            for word in re.findall(w, line) :
                if word in counts["word"] :
                    counts["word"][word] += 1
                else :
                    counts["word"][word] = 1
    print_word_count(counts)


    '''
        Now we are accessing the individual lines. We can create a function that will contain all of the individual words. Here the strat might just be to use a dictionary as well as a function to count based on that dictionary.
    '''

if __name__ == '__main__' :
    main()