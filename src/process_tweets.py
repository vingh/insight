#! python
__author__ = 'Vinod Kumar'
'''*******************************************************************************************************************
This program is written to in response insight code challenge.
Challenge is to implement two features:
    1. Calculate the total number of times each word has been tweeted.
    2. Calculate the median number of unique words per tweet, and update this median as tweets come in.
*******************************************************************************************************************'''

import statistics               #module import for median calculation
from collections import Counter #module import for maintaining lists

#def process(self, if1, of1, of2):
wordscount = Counter()           #dict hash object with key & value, for keeping track of words and count
#open files with 'with' statement. No need for close.
with open("./tweet_input/tweets.txt", "r", encoding='utf-8') as ifile1, open("./tweet_output/ft2.txt", "w", encoding='utf-8') as ofile2:
    twords =  Counter().clear()         #new hash table for counting unique words and their occurance per each line
    twt_word_cnt = []                   #initialization of list for storing unique words in a line
    for line in ifile1:                 #read through input file, line by line, loops through end of file. Below indent statements will be executed in loop.
        twords =  Counter(line.split()) #uses built-in function to split on whitespace, default function
        twt_word_cnt.append(len(twords))#inserts number of unique words in
        wordscount.update(twords)       #increment unique words and their count to hash
        ofile2.writelines("%.2f \n" % statistics.median(twt_word_cnt)) #calculates median on list values using built-in function and write median to file in 2 decimal format.

#opens file for storing unique words and count
with open("./tweet_output/ft1.txt", "w", encoding='utf-8') as ofile1:
    for item in sorted(wordscount.items()):             #loops through hash objects
        ofile1.writelines("{}\t{}".format(*item) + "\n")#writes hash key & value i.e unique word and its occurance across tweets to output file.

    #end_of_file




