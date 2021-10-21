import nltk
import json
import random
import string
from nltk.corpus import brown

# get the brown corpus
brown_tagged_sents = brown.tagged_sents()
#brown_sents = brown.sents()

# divided to train and test parts
size = int(len(brown_tagged_sents) * 0.95)
train_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]

# combining tagger using DefaultTagger, UnigramTagger and BigramTagger
t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(train_sents, backoff=t0)
t2 = nltk.BigramTagger(train_sents, backoff=t1)

# regular expression tagger
regexp_tagger = nltk.RegexpTagger(
    [(r'^-?[0-9]+(.[0-9]+)?$', 'CD'),  # cardinal numbers
     (r'(The|the|A|a|An|an)$', 'AT'),  # articles
     (r'.*able$', 'JJ'),  # adjectives
     (r'.*ness$', 'NN'),  # nouns formed from adjectives
     (r'.*ly$', 'RB'),  # adverbs
     (r'.*s$', 'NNS'),  # plural nouns
     (r'.*ing$', 'VBG'),  # gerunds
     (r'.*ed$', 'VBD'),  # past tense verbs
     (r'.*es$', 'VBZ'),  # 3rd singular present
     (r'.*ould$', 'MD'),  # modals
     (r'.*', 'NN')  # nouns (default)
     ])

# evaluate the 2 taggers
eval1 = t2.evaluate(test_sents)
eval2 = regexp_tagger.evaluate(test_sents)
print('evaluate combining tagger:', eval1)
print('evaluate regular expression tagger:', eval2)

# get random 5 reviews
COUNT = 5
random_list = sorted(random.sample(range(0, 8635403), COUNT))
reviews = []
line_count = 0
with open('yelp_academic_dataset_review.json', encoding='utf-8') as f:
    for line in f:
        line_contents = json.loads(line)
        if line_count in random_list:
            reviews.append(line_contents['text'])
            #print(line_count)
            if line_count == random_list[COUNT - 1]:
                break
        line_count += 1

# get excluded_words for token
excluded_words_list = []
for p in string.punctuation:
    excluded_words_list.append(p)
excluded_words_list.append('\'s')
excluded_words_list.append('n\'t')
excluded_words_list.append("''")
excluded_words_list.append("``")

with open('pos_tagging.txt', 'w', encoding='utf-8') as f:
    for review in reviews:
        # token the sentences
        tokens = nltk.word_tokenize(review)
        words = [word for word in tokens if word not in excluded_words_list]
        # use conbining_tagger and regexp_tagger to tag
        combining_tagger_result = t2.tag(words)
        regexp_tagger_result = regexp_tagger.tag(words)
        # print the tagging result
        print('combining_tagger_result:', combining_tagger_result)
        print('regexp_tagger_result:', regexp_tagger_result)
        f.write(str(combining_tagger_result))
        f.write('\n')
        f.write(str(regexp_tagger_result))
        f.write('\n')





