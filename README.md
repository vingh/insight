# insight

<B>Insight Data Engineering - Coding Challenge</B>

Challenge is to implement two features:

    1. Calculate the total number of times each word has been tweeted.

    2. Calculate the median number of unique words per tweet, and update this median as tweets come in.

*******************************************************************************************************************'''


Run 'run.sh' for execution of python program: process_tweets.py

program expects tweets.txt in in tweets_input folder, with tweets. File is read using utf-8 rather than ascii, with this option ascii would work too.

Output of task-1, total number of times each word has been tweeted, would be written to tweet_output/ft1.txt

Output of task-2, median number of unique words per tweet, would be written to tweet_output/ft2.txt

Benchmark testing done using 111k tweets. Scipy- Took under 10 minutes to process. Numpy took 10+ minutes and collections took above 1hour.

Future suggestions: 

1. Task-1, explore the option of writing words count to file sequentially. Insert for new words, update count for existing.

2. Task-2, explore the option of skip lists (or dynamic lits) and algo suggested by soumya per below reference.
    Efficient Algorithm for Computing a Running Median by Soumya Mohanty. https://dcc.ligo.org/T030168/public
