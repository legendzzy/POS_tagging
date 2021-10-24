NLTK library installing link: https://www.nltk.org/install.html
Python version: 3.6, 3.7, 3.8, or 3.9

usage of POS tagging:
Put pos_tagging.py and yelp_academic_dataset_review.json under the same path, then run pos_tagging.py.
Then the results will be printed, and the results are also saved in pos_tagging.txt.

Explanations of sample output:
There are 10 lines of tagging result, with two tagging methods. The first is combining tagger, the second is regular expression tagger.
They both do test on 5 sentences of review extracted from the yelp_academic_dataset_review.json.
One sample output is shown as below:

[('I', 'PPSS'), ('do', 'DO'), ('know', 'VB'), ('if', 'CS'), ('any', 'DTI'), ('of', 'IN'), ('you', 'PPO'), ('remember', 'VB'), ('when', 'WRB'), ('Steamhouse', 'NN'), ('Lounge', 'NN-TL'), ('was', 'BEDZ'), ('in', 'IN'), ('Buckhead', 'NP'), ('but', 'CC'), ('it', 'PPS'), ('was', 'BEDZ'), ('a', 'AT'), ('favorite', 'JJ'), ('place', 'NN'), ('for', 'IN'), ('my', 'PP$'), ('friends', 'NNS'), ('and', 'CC'), ('I', 'PPSS'), ('to', 'TO'), ('go', 'VB'), ('on', 'IN'), ('Sunday', 'NR'), ('afternoons', 'NNS'), ('for', 'IN'), ('the', 'AT'), ('lobster', 'NN'), ('bisque', 'NN'), ('raw', 'JJ'), ('oysters', 'NNS'), ('and', 'CC'), ('bloody', 'JJ'), ('mary', 'NN')]
[('I', 'NN'), ('do', 'NN'), ('know', 'NN'), ('if', 'NN'), ('any', 'NN'), ('of', 'NN'), ('you', 'NN'), ('remember', 'NN'), ('when', 'NN'), ('Steamhouse', 'NN'), ('Lounge', 'NN'), ('was', 'NNS'), ('in', 'NN'), ('Buckhead', 'NN'), ('but', 'NN'), ('it', 'NN'), ('was', 'NNS'), ('a', 'AT'), ('favorite', 'NN'), ('place', 'NN'), ('for', 'NN'), ('my', 'NN'), ('friends', 'NNS'), ('and', 'NN'), ('I', 'NN'), ('to', 'NN'), ('go', 'NN'), ('on', 'NN'), ('Sunday', 'NN'), ('afternoons', 'NNS'), ('for', 'NN'), ('the', 'AT'), ('lobster', 'NN'), ('bisque', 'NN'), ('raw', 'NN'), ('oysters', 'NNS'), ('and', 'NN'), ('bloody', 'NN'), ('mary', 'NN')]
[('Excellent', 'JJ'), ('choice', 'NN'), ('for', 'IN'), ('Monday', 'NR'), ('night', 'NN'), ('dinner', 'NN')]
[('Excellent', 'NN'), ('choice', 'NN'), ('for', 'NN'), ('Monday', 'NN'), ('night', 'NN'), ('dinner', 'NN')]
[('I', 'PPSS'), ('like', 'VB'), ('to', 'TO'), ('walk', 'VB'), ('around', 'RB'), ('my', 'PP$'), ('house', 'NN'), ('barefoot', 'JJ')]
[('I', 'NN'), ('like', 'NN'), ('to', 'NN'), ('walk', 'NN'), ('around', 'NN'), ('my', 'NN'), ('house', 'NN'), ('barefoot', 'NN')]
[('Took', 'VBD'), ('longer', 'JJR'), ('than', 'CS'), ('expected', 'VBN')]
[('Took', 'NN'), ('longer', 'NN'), ('than', 'NN'), ('expected', 'VBD')]
[('We', 'PPSS'), ('booked', 'VBN'), ('a', 'AT'), ('reservation', 'NN'), ('at', 'IN'), ('the', 'AT'), ('restaurant', 'NN'), ('2', 'CD'), ('days', 'NNS'), ('prior', 'RB'), ('to', 'IN'), ('our', 'PP$'), ('evening', 'NN'), ('at', 'IN'), ('the', 'AT'), ('Atlantic', 'JJ-TL'), ('Fish', 'NP'), ('Company', 'NN-TL')]
[('We', 'NN'), ('booked', 'VBD'), ('a', 'AT'), ('reservation', 'NN'), ('at', 'NN'), ('the', 'AT'), ('restaurant', 'NN'), ('2', 'CD'), ('days', 'NNS'), ('prior', 'NN'), ('to', 'NN'), ('our', 'NN'), ('evening', 'VBG'), ('at', 'NN'), ('the', 'AT'), ('Atlantic', 'NN'), ('Fish', 'NN'), ('Company', 'NN')]

