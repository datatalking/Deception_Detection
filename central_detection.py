# SOURCE https://towardsdatascience.com/media-bias-detection-using-deep-learning-libraries-in-python-44efef4918d1
# SOURCE https://www.kaggle.com/snapcrack/all-the-news
# sentiment analysis https://towardsdatascience.com/all-the-news-17fa34b52b9d

# DATA SOURCE https://components.one/datasets/all-the-news-articles-dataset/
# stemming process

import nltk
from nltk import pos_tag
from nltk.stem import PorterStemmer
from nltk import word_tokenize
from collections import Counter
import time

stemmer = PorterStemmer()
tokenizer = nltk.data.load(‘tokenizers / punkt / english.pickle’)
progress = 0  # for keeping track of where the function is


def stem(x):
	end = time.time()
	dirty = word_tokenize(x)
	tokens = []
	for word in dirty:
		if word.strip(‘.’) == ‘’:  # this deals with the bug
			pass
		elif re.search(r’\d{1, }’, word):  # getting rid of digits
			pass
	else:
		tokens.append(word.strip(‘.’))
		global start
		global progress
		tokens = pos_tag(tokens)  #
		progress += 1
		stems = ‘ ‘.join(
			stemmer.stem(key.lower()) for key, value in tokens if value != ‘NNP’)  # getting rid of proper nouns
		
		end = time.time()
		sys.stdout.write(‘\r
		{}
		percent, {}
		position, {}
		per
		second ‘.format(str(float(progress / len(articles))),
		                str(progress), (1 / (end — start))))  # lets us see how much time is left
		start = time.time()
		return stems
	start = time.time()
	articles['stems'] = articles.content.apply(lambda x: stem(x))